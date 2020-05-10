# -*- coding:utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication([])

# Qt应用在窗口都关闭的时候会自动退出，以下将设置此功能
app.setQuitOnLastWindowClosed(False)

# 图标
sPath = "D:\\Learning\\trunk\\QT\\PyQT\\img\\icon.png"
icon = QIcon(sPath)

clipboard = QApplication.clipboard()
dialog = QColorDialog()


def copy_color_hex():
    if dialog.exec_():
        color = dialog.currentColor()
        clipboard.setText(color.name())


def copy_color_rgb():
    if dialog.exec_():
        color = dialog.currentColor()
        clipboard.setText("rgb(%d, %d, %d)" % (
            color.red(), color.green(), color.blue()
        ))


def copy_color_hsv():
    if dialog.exec_():
        color = dialog.currentColor()
        clipboard.setText("hsv(%d, %d, %d)" % (
            color.hue(), color.saturation(), color.value()
        ))


# 创建托盘图标
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

menu = QMenu()

#一种创建QAction的方式
action1 = QAction("Hex")
action1.triggered.connect(copy_color_hex)
menu.addAction(action1)

#另一种创建QAction的方式
action2 = menu.addAction("RGB")
action2.triggered.connect(copy_color_rgb)


action3 = QAction("HSV")
action3.triggered.connect(copy_color_hsv)
menu.addAction(action3)

action4 = QAction("Quit")
action4.triggered.connect(app.quit)
menu.addAction(action4)

tray.setContextMenu(menu)

app.exec_()
