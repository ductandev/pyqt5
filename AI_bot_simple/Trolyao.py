# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Trolyao.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(510, 586)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Tom_chat = QtWidgets.QLabel(self.centralwidget)
        self.Tom_chat.setGeometry(QtCore.QRect(70, 30, 371, 181))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.Tom_chat.setFont(font)
        self.Tom_chat.setFrameShape(QtWidgets.QFrame.Box)
        self.Tom_chat.setLineWidth(2)
        self.Tom_chat.setObjectName("Tom_chat")
        self.Me_chat = QtWidgets.QLabel(self.centralwidget)
        self.Me_chat.setGeometry(QtCore.QRect(70, 280, 371, 181))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.Me_chat.setFont(font)
        self.Me_chat.setFrameShape(QtWidgets.QFrame.Box)
        self.Me_chat.setLineWidth(2)
        self.Me_chat.setObjectName("Me_chat")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 10, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 250, 55, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Button.setGeometry(QtCore.QRect(90, 500, 93, 28))
        self.Start_Button.setObjectName("Start_Button")
        self.Stop_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Stop_Button.setGeometry(QtCore.QRect(340, 500, 93, 28))
        self.Stop_Button.setObjectName("Stop_Button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 510, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Tom_chat.setText(_translate("MainWindow", "...."))
        self.Me_chat.setText(_translate("MainWindow", "...."))
        self.label_3.setText(_translate("MainWindow", "Tom"))
        self.label_4.setText(_translate("MainWindow", "Me"))
        self.Start_Button.setText(_translate("MainWindow", "Start"))
        self.Stop_Button.setText(_translate("MainWindow", "Stop"))
