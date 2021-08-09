# cach 1 chay code truc tiep bang file ".ui" nho thay ten file ".ui" dong 5
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("cach_1.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()
