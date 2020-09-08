# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QFirstScroll(object):
    def setupUi(self, QFirstScroll):
        QFirstScroll.setObjectName("QFirstScroll")
        QFirstScroll.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(QFirstScroll)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 776, 525))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.addWidget(self.scrollArea)
        QFirstScroll.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(QFirstScroll)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        QFirstScroll.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(QFirstScroll)
        self.statusbar.setObjectName("statusbar")
        QFirstScroll.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(QFirstScroll)
        self.pushButton.pressed.connect(self.label.clear)
        QtCore.QMetaObject.connectSlotsByName(QFirstScroll)

    def retranslateUi(self, QFirstScroll):
        _translate = QtCore.QCoreApplication.translate
        QFirstScroll.setWindowTitle(_translate("QFirstScroll", "QFirstScroll"))
        self.label.setText(_translate("QFirstScroll", "11111"))
        self.pushButton.setText(_translate("QFirstScroll", "PushButton"))
        self.label_2.setText(_translate("QFirstScroll", "TextLabel"))
        self.label_3.setText(_translate("QFirstScroll", "TextLabel"))
        self.label_4.setText(_translate("QFirstScroll", "TextLabel"))
        self.menu.setTitle(_translate("QFirstScroll", "顶顶顶顶顶"))
        self.menu_2.setTitle(_translate("QFirstScroll", "发生发"))
