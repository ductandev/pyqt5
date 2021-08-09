# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nhieu_screen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.home)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.home)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.home)
        self.screen1 = QtWidgets.QWidget()
        self.screen1.setObjectName("screen1")
        self.label_2 = QtWidgets.QLabel(self.screen1)
        self.label_2.setGeometry(QtCore.QRect(280, 170, 211, 151))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.stackedWidget.addWidget(self.screen1)
        self.screen2 = QtWidgets.QWidget()
        self.screen2.setObjectName("screen2")
        self.label_3 = QtWidgets.QLabel(self.screen2)
        self.label_3.setGeometry(QtCore.QRect(260, 210, 261, 131))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.screen2)
        self.screen3 = QtWidgets.QWidget()
        self.screen3.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.screen3.setObjectName("screen3")
        self.label_4 = QtWidgets.QLabel(self.screen3)
        self.label_4.setGeometry(QtCore.QRect(210, 120, 231, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stackedWidget.addWidget(self.screen3)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 4)
        self.home_Button = QtWidgets.QPushButton(self.centralwidget)
        self.home_Button.setObjectName("home_Button")
        self.gridLayout.addWidget(self.home_Button, 1, 0, 1, 1)
        self.Screen1_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Screen1_Button.setObjectName("Screen1_Button")
        self.gridLayout.addWidget(self.Screen1_Button, 1, 1, 1, 1)
        self.Screen2_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Screen2_Button.setObjectName("Screen2_Button")
        self.gridLayout.addWidget(self.Screen2_Button, 1, 2, 1, 1)
        self.Screen3_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Screen3_Button.setObjectName("Screen3_Button")
        self.gridLayout.addWidget(self.Screen3_Button, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.home_Button.clicked.connect(self.show_home_creen)
        self.Screen1_Button.clicked.connect(self.show_creen1)
        self.Screen2_Button.clicked.connect(self.show_creen2)
        self.Screen3_Button.clicked.connect(self.show_creen3)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Chính"))
        self.label_2.setText(_translate("MainWindow", "hình 1"))
        self.label_3.setText(_translate("MainWindow", "hình 2"))
        self.label_4.setText(_translate("MainWindow", "hình 3"))
        self.home_Button.setText(_translate("MainWindow", "Home"))
        self.Screen1_Button.setText(_translate("MainWindow", "Screen 1"))
        self.Screen2_Button.setText(_translate("MainWindow", "Screen 2"))
        self.Screen3_Button.setText(_translate("MainWindow", "Screen 3"))

    def show_home_creen(self):
        self.stackedWidget.setCurrentWidget(self.home)
    def show_creen1(self):
        self.stackedWidget.setCurrentWidget(self.screen1)
    def show_creen2(self):
        self.stackedWidget.setCurrentWidget(self.screen2)
    def show_creen3(self):
        self.stackedWidget.setCurrentWidget(self.screen3)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
