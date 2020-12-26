# -*- coding:utf-8 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        # self.setVHLayout()
        # self.setNestLayout()
        # self.setGridLayout()
        # self.setStackedLayout()
        # self.stackedLayuotTabExample()
        self.useQTabWidget()


    def setVHLayout(self):
        # layout = QVBoxLayout()
        layout = QHBoxLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def setNestLayout(self):
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout(layout2)  # 添加嵌套布局

        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))

        layout1.addLayout(layout3)
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(20)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

    def setGridLayout(self):
        """您可以为每个小部件指定行和列的位置。
        您可以跳过元素，它们将保留为空。"""
        layout = QGridLayout()

        layout.addWidget(Color('red'), 0, 0)
        layout.addWidget(Color('green'), 1, 0)
        layout.addWidget(Color('blue'), 1, 1)
        layout.addWidget(Color('purple'), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def setStackedLayout(self):
        """此布局使您可以将元素直接放置在彼此的前面。
        然后，您可以选择要显示的窗口小部件。
        您可以将其用于在图形应用程序中绘制图层，或模仿类似标签的界面。
        """
        layout = QStackedLayout()

        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('yellow'))

        layout.setCurrentIndex(3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def stackedLayuotTabExample(self):
        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        layout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(layout)

        for n, color in enumerate(['red', 'green', 'blue', 'yellow']):
            btn = QPushButton(str(color))
            btn.pressed.connect(lambda n=n: layout.setCurrentIndex(n))
            button_layout.addWidget(btn)
            layout.addWidget(Color(color))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)

    def useQTabWidget(self):
        tabs = QTabWidget()
        tabs.setDocumentMode(False)
        tabs.setTabPosition(QTabWidget.East)
        tabs.setMovable(False)

        for n, color in enumerate(['red', 'green', 'blue', 'yellow']):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)

app = QApplication([])

window = MainWindow()
window.show()

app.exec_()
