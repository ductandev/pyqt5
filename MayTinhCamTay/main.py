import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from maytinh import  Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()       # 
        self.ui = Ui_MainWindow()           # nhảy vào "class Ui_MainWindow": bên file maytinh.py
        self.ui.setupUi(self.main_win)      # Tất cả các code dồn hết vào cho main_win
    

        self.ui.Button_0.clicked.connect(lambda: self.pressed_it("0"))      # lambda: lệnh thực thi
        self.ui.Button_1.clicked.connect(lambda: self.pressed_it("1"))
        self.ui.Button_2.clicked.connect(lambda: self.pressed_it("2"))
        self.ui.Button_3.clicked.connect(lambda: self.pressed_it("3"))       
        self.ui.Button_4.clicked.connect(lambda: self.pressed_it("4"))
        self.ui.Button_5.clicked.connect(lambda: self.pressed_it("5"))
        self.ui.Button_6.clicked.connect(lambda: self.pressed_it("6"))
        self.ui.Button_7.clicked.connect(lambda: self.pressed_it("7"))
        self.ui.Button_8.clicked.connect(lambda: self.pressed_it("8"))
        self.ui.Button_9.clicked.connect(lambda: self.pressed_it("9"))
        self.ui.Percent_Button.clicked.connect(lambda: self.pressed_it("%"))
        self.ui.Clear_Button.clicked.connect(lambda: self.pressed_it("C"))
        self.ui.Arrow_Button.clicked.connect(lambda: self.pressed_Arrow())
        self.ui.Devide_Button.clicked.connect(lambda: self.pressed_it("/"))
        self.ui.Multiply_Button.clicked.connect(lambda: self.pressed_it("*"))
        self.ui.Minus_Button.clicked.connect(lambda: self.pressed_it("-"))
        self.ui.Add_Button.clicked.connect(lambda: self.pressed_it("+"))
        self.ui.Equal_Button.clicked.connect(lambda: self.pressed_Equal())
        self.ui.Decimal_Button.clicked.connect(lambda: self.pressed_it("."))
        self.ui.Plus_Minus_Button.clicked.connect(lambda: self.pressed_Plus_Minus())

    def pressed_Equal(self):
        screen_1 = self.ui.Screen.text()            #**same
        try:
            result = eval(screen_1)                     # lệnh cộng,trừ,nhân,chia chỉ 1 dòng lấy tất cả ký tự trên đó làm toán luôn
            self.ui.Screen.setText(str(result))
        except:
            self.ui.Screen.setText("error")

    def pressed_Plus_Minus(self):
        screen_1 = self.ui.Screen.text()            #**same
        if "-" in screen_1:
            self.ui.Screen.setText(screen_1.replace("-", ""))
        else:
            self.ui.Screen.setText(f'-{screen_1}')

    def pressed_Arrow(self):
        screen_1 = self.ui.Screen.text()            #**same
        screen_1 = screen_1[:-1]
        self.ui.Screen.setText(screen_1)

    def pressed_it(self, pressed):
        if pressed == "C":
            self.ui.Screen.setText("0")
        else:
            if self.ui.Screen.text() == "0":
                self.ui.Screen.setText("")
            self.ui.Screen.setText(f'{self.ui.Screen.text()}{pressed}')     # self.ui.Screen.text(): lấy số tiếp theo 


    def show(self):                         # show giao diện của main_win
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())

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