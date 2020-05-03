# -*- coding:utf-8 -*-
"""
用户与Qt应用程序进行的每次交互都会导致一个事件。
事件有多种类型，每种类型代表不同的交互类型，例如鼠标或键盘事件。

发生的事件将传递到发生交互的窗口小部件上的特定于事件的处理程序。
例如，单击窗口小部件将导致QMouseEvent将发送到.mousePressEvent窗口小部件上的事件处理程序。
该处理程序可以查询事件以找出信息，例如触发事件的原因以及发生的具体位置。

Qt的信号与槽机制使得开发者能够很方便的将回调函数与UI事件绑定到一起
"""

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title will be passed to the function.
        self.windowTitleChanged.connect(self.onWindowTitleChange)

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is discarded in the lambda and the
        # function is called without parameters.
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is passed to the function
        # and replaces the default parameter
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))

        # SIGNAL: The connected function will be called whenever the window
        # title is changed. The new title is passed to the function
        # and replaces the default parameter. Extra data is passed from
        # within the lambda.
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))

        self.setWindowTitle("My Awesome App")

        label = QtWidgets.QLabel("THIS IS AWESOME!!!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

    # SLOT: This accepts a string, e.g. the window title, and prints it
    def onWindowTitleChange(self, s):
        print(s)

    # SLOT: This has default parameters and can be called without a value
    def my_custom_fn(self, a="HELLLO!", b=5):
        print(a, b)

    def contextMenuEvent(self, event):
        print("Context menu event!")
        super(MainWindow, self).contextMenuEvent(event)


class CustomButton(QtWidgets.QPushButton):

    def event(self, e):
        print('click click')
        e.accept()  # 传递结束


class CustomIgnoreButton(QtWidgets.QPushButton):
    def event(self, e):
        e.ignore()  # 向父级传递


app = QtWidgets.QApplication([])
window = MainWindow()
window.show()

app.exec()
