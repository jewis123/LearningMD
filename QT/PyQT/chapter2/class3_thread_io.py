# -*- coding:utf-8 -*-
"""
有时能够传回正在运行的工作程序的状态和数据很有帮助。
这可能包括计算结果，提出的例外情况或正在进行的进度（请考虑进度条）。
Qt提供了信号和插槽框架，它使您能够做到这一点，并且是线程安全的，从而允许从运行中的线程直接与GUI前端进行安全通信。
信号允许您输入.emit值，然后通过已与链接的插槽函数在代码的其他位置提取这些值.connect。
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import time
import traceback
import sys


class WorkerSignals(QObject):
    '''
    自定义信号只能在从“ QObject”派生的对象上定义。
    由于QRunnable不是从QObject派生的，因此我们无法直接在其中定义信号。
    自定义QObject来保存信号是最简单的解决方案。
    '''
    finished = pyqtSignal()  # no data
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)  # data return from processing , anything
    progress = pyqtSignal(int)  # 定义信号传递一个整型代表进度


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress

    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        b.pressed.connect(self.oh_no)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.threadpool = QThreadPool()
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def oh_no(self):
        # Pass the function to execute
        worker = Worker(self.execute_this_fn)  # Any other args, kwargs are passed to the run function
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)

        # Execute
        self.threadpool.start(worker)

    def progress_fn(self, n):
        print("%d%% done" % n)

    def execute_this_fn(self, progress_callback):
        for n in range(0, 5):
            time.sleep(1)
            progress_callback.emit(n * 100 / 4)

        return "Done."

    def print_output(self, s):
        print(s)

    def thread_complete(self):
        print("THREAD COMPLETE!")

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication([])
window = MainWindow()
app.exec_()

"""
点评：
we are still making use of the event loop (and the GUI thread) to process the output of our workers.

This isn't a problem when we're simply tracking progress, completion or returning metadata. 
However, if you have workers which return large amounts of data 
— e.g. loading large files, performing complex analysis and need (large) results, or querying databases 
— passing this data back through the GUI thread may cause performance problems and is best avoided.

Similarly, if your application makes use of a large number of threads and Python result handlers, 
you may come up against the limitations of the GIL. 
As mentioned previously, when using threads execution of Python is limited to a single thread at one time. 
The Python code that handles signals from your threads can be blocked by your workers and vice versa.
 Since blocking your slot functions blocks the event loop, this can directly impact GUI responsiveness.

In these cases it is often better to investigate using a pure-Python thread pool 
(e.g. concurrent futures) to keep your processing and thread-event handling further isolated from your GUI. 
However, note that any Python GUI code can block other Python code unless it's in a separate process.
"""
