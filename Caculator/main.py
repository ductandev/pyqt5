import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from Caculator import Ui_MainWindow

class MainWinDow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.ui.Plus_Button.clicked.connect(self.Plus_Equal)
        self.ui.Minus_Button.clicked.connect(self.Minus_Equal)
        self.ui.Multiply_Button.clicked.connect(self.Multyply_Equal)
        self.ui.Devide_Button.clicked.connect(self.Devide_Equal)
    
    def Plus_Equal(self):
        Addnumber = self.ui.Screen_1.toPlainText() + "+" + self.ui.Screen_2.toPlainText()
        try:
            result = eval(Addnumber)
            self.ui.Screen_3.setText(str(result))
        except:
            self.ui.Screen_3.setText("error")

    def Minus_Equal(self):
        Minusnumber = self.ui.Screen_1.toPlainText() + "-" + self.ui.Screen_2.toPlainText()
        try:
            result = eval(Minusnumber)
            self.ui.Screen_3.setText(str(result))
        except:
            self.ui.Screen_3.setText("error")

    def Multyply_Equal(self):
        Mutiplynumber = self.ui.Screen_1.toPlainText() + "*" + self.ui.Screen_2.toPlainText()
        try:
            result = eval(Mutiplynumber)
            self.ui.Screen_3.setText(str(result))
        except:
            self.ui.Screen_3.setText("error")

    def Devide_Equal(self):
        Devidenumber = self.ui.Screen_1.toPlainText() + "/" + self.ui.Screen_2.toPlainText()
        try:
            result = eval(Devidenumber)
            self.ui.Screen_3.setText(str(result))
        except:
            self.ui.Screen_3.setText("error")

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWinDow()
    main_win.show()
    sys.exit(app.exec_())
