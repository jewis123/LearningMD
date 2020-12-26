# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time

class Worker(QRunnable):
    '''
    QRunnable：要执行的工作的容器
    '''

    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        self.fn(*self.args, **self.kwargs)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.counter = 0

        layout = QVBoxLayout()

        self.l = QLabel("Start")
        b = QPushButton("DANGER!")
        # b.pressed.connect(self.sleep)
        b.pressed.connect(self.sleepByThread)

        layout.addWidget(self.l)
        layout.addWidget(b)

        w = QWidget()
        w.setLayout(layout)

        self.setCentralWidget(w)

        self.show()

        self.threadpool = QThreadPool() # QThreadPool：将工作传递给备用线程的方法
        print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount()) #超过线程池上线将排队

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)
        self.timer.start()

    def sleep(self):
        print('Start Thread')
        time.sleep(5)
        print("End Thread")

    def sleepByThread(self):
        """开启进程处理其他事务"""
        worker = Worker(self.sleep)
        self.threadpool.start(worker)

    def recurring_timer(self):
        self.counter += 1
        self.l.setText("Counter: %d" % self.counter)


app = QApplication([])
window = MainWindow()
app.exec_()