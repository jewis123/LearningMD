# -*- coding:utf-8 -*-
import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication([])


## 方法一：直接加载
# window = uic.loadUi("form.ui")

## 方法二：在现有Widget中加载ui
# class MainWindow(QtWidgets.QMainWindow):
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         uic.loadUi("mainwindow.ui", self)
# window = MainWindow()

## 方法三：让界面集成翻译自ui的py界面
from .Form import Ui_QFirstScroll
class MainWindow(QtWidgets.QMainWindow, Ui_QFirstScroll):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
window = MainWindow()


window.show()
app.exec_()
