# -*- coding:utf-8 -*-
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class CustomDialog(QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("HELLO!")

        QBtn = QDialogButtonBox.Cancel | QDialogButtonBox.Ok | QDialogButtonBox.Yes  # 创建两个对话框按钮，顺序无影响

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        sPath = "D:\\Learning\\trunk\\QT\\PyQT\\img\\icon.png"
        button_action = QAction(QIcon(sPath), "Your button", self)
        button_action.setStatusTip("This is Status Tip")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(False)

        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)

        # dlg = QDialog(self)  # 创建一个Dialog，并将父控件设置为主窗口
        dlg = CustomDialog(self)
        dlg.setWindowTitle("HELLO!")

        # 这里会打断主窗口的事件循环
        # 任何时候都只能运行一个Qt事件循环！QDialog完全阻止您的应用程序执行。多线程下则不存在这个问题
        # dlg.exec_()

        if dlg.exec_():  # 接受对话框按钮结果
            print("Success!")
        else:
            print("Cancel!")


app = QApplication([])

window = MainWindow()
window.show()

app.exec_()
