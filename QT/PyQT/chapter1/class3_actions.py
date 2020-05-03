# -*- coding:utf-8 -*-

"""
QAction是提供描述抽象用户界面的方法的类。
有了QAction，开发者能够一次性地去定义一个动作要执行的内容，而不在每次用到这个动作的地方去反复定义
"""
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import \
    QMainWindow, \
    QLabel, \
    QToolBar, \
    QApplication, \
    QAction, \
    QStatusBar,\
    QCheckBox

from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        label = QLabel("THIS IS AWESOME!!!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        sPath = "D:\\Learning\\trunk\\QT\\PyQT\\img\\icon.png"
        button_action = QAction(QIcon(sPath), "Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon(sPath), "Your button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication([])
window = MainWindow()
window.show()

app.exec()
