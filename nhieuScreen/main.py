# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nhieu_screen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from nhieu_screen import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()           #2
        self.ui = Ui_MainWindow()               #3
        self.ui.setupUi(self.main_win)          #4
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)


        self.ui.home_Button.clicked.connect(self.show_home_creen)
        self.ui.Screen1_Button.clicked.connect(self.show_creen1)
        self.ui.Screen2_Button.clicked.connect(self.show_creen2)
        self.ui.Screen3_Button.clicked.connect(self.show_creen3)


    def show(self):
        self.main_win.show()                    #5
    
    def show_home_creen(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
    def show_creen1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.screen1)
    def show_creen2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.screen2)
    def show_creen3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.screen3)

if __name__ == "__main__":                      #start
    app = QApplication(sys.argv)                #1
    main_win = MainWindow()                     #----> nhảy vào "class MainWindow:""
    main_win.show()                             #5
    sys.exit(app.exec_())                        #6


#  ** Một Chương Trình Bắt Buộc Gồm Có**
#'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)      #1
    MainWindow = QtWidgets.QMainWindow()        #2
    ui = Ui_MainWindow()                        #3
    ui.setupUi(MainWindow)                      #4
    MainWindow.show()                           #5
    sys.exit(app.exec_())                       #6
#'''