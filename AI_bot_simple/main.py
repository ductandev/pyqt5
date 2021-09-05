import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from Trolyao import Ui_MainWindow
import speech_recognition
import pyttsx3                              # thư viện chuyển chữ thành giọng nói

Tom_ear = speech_recognition.Recognizer()
Tom_mouth = pyttsx3.init()


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()       # 
        self.ui = Ui_MainWindow()           # nhảy vào "class Ui_MainWindow": bên file Trolyao.py
        self.ui.setupUi(self.main_win)      # Tất cả các code dồn hết vào cho main_win
        self.ui.Start_Button.clicked.connect(lambda: self.Start_AI())
        self.ui.Stop_Button.clicked.connect(lambda: self.main_win.close())
    
    def Start_AI(self):
        with speech_recognition.Microphone() as mic:
            audio = Tom_ear.listen(mic)
        try:
            you = Tom_ear.recognize_google(audio)
            self.ui.Me_chat.setText(str(you))
        except:
            you = ""
        if "hello Tom" in you:
            Tom_brain = "hi life"
            Tom_mouth.say(Tom_brain)
            Tom_mouth.runAndWait()
            while True:
                with speech_recognition.Microphone() as mic:
                    audio = Tom_ear.listen(mic)
                try:
                    you = Tom_ear.recognize_google(audio)
                    self.ui.Me_chat.setText(str(you))
                except:
                    you = ""
                if you == "":
                    Tom_brain = "i can't hear you, try again"
                elif "hello" in you:
                    Tom_brain = "hello life"
                elif "doing" in you:
                    Tom_brain = "i'm sleeping"
                elif "sure" in you:
                    Tom_brain = "i'm not sure"
                elif "nice" in you:
                    Tom_brain = "nice to see you too"
                elif "bye" in you:
                    Tom_brain = "goodbye life"
                    self.ui.Tom_chat.setText(str(Tom_brain))
                    Tom_mouth.say(Tom_brain)
                    Tom_mouth.runAndWait()
                    break
                else:
                    Tom_brain = "oh thank you"
                self.ui.Tom_chat.setText(str(Tom_brain))
                Tom_mouth.say(Tom_brain)
                Tom_mouth.runAndWait()

    def show(self):
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
