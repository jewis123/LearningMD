# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("First Window")

        label = QLabel("This is a label")

        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)


app = QApplication([])
window = MainWindow()
window.show()

app.exec()
