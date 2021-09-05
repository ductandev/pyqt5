# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Caculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 397)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Screen_3 = QtWidgets.QLabel(self.centralwidget)
        self.Screen_3.setGeometry(QtCore.QRect(30, 200, 401, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Screen_3.setFont(font)
        self.Screen_3.setFrameShape(QtWidgets.QFrame.Box)
        self.Screen_3.setLineWidth(3)
        self.Screen_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Screen_3.setObjectName("Screen_3")
        self.Plus_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Plus_Button.setGeometry(QtCore.QRect(20, 300, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Plus_Button.setFont(font)
        self.Plus_Button.setObjectName("Plus_Button")
        self.Minus_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Minus_Button.setGeometry(QtCore.QRect(130, 300, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Minus_Button.setFont(font)
        self.Minus_Button.setObjectName("Minus_Button")
        self.Multiply_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Multiply_Button.setGeometry(QtCore.QRect(240, 300, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Multiply_Button.setFont(font)
        self.Multiply_Button.setObjectName("Multiply_Button")
        self.Devide_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Devide_Button.setGeometry(QtCore.QRect(350, 300, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Devide_Button.setFont(font)
        self.Devide_Button.setObjectName("Devide_Button")
        self.Screen_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.Screen_1.setGeometry(QtCore.QRect(30, 20, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Screen_1.setFont(font)
        self.Screen_1.setObjectName("Screen_1")
        self.Screen_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.Screen_2.setGeometry(QtCore.QRect(30, 110, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Screen_2.setFont(font)
        self.Screen_2.setObjectName("Screen_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 26))
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
        self.Screen_3.setText(_translate("MainWindow", "0"))
        self.Plus_Button.setText(_translate("MainWindow", "Plus"))
        self.Minus_Button.setText(_translate("MainWindow", "Minus"))
        self.Multiply_Button.setText(_translate("MainWindow", "Multiply"))
        self.Devide_Button.setText(_translate("MainWindow", "Devide"))
