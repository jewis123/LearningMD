# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import (QWidget, QApplication,QLabel, QScrollArea, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()
        for i in range(1,50):
            object = QLabel("TextLabel")
            self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 1000, 900)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()

app = QApplication([])
main = MainWindow()
app.exec_()