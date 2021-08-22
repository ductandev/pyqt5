# PyQt examples 2021
- https://github.com/pyqt/examples

# Có 2 cách để chạy chương trình pyqt5
### Cách 1 : chạy trực tiếp file ".ui"
from PyQt5 import uic \
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("file.ui")

app = QApplication([]) \
window = Window() \
form = Form()  \
form.setupUi(window)  \
window.show() \
app.exec()

### Cách 2 : đổi đuôi ".ui" thành ".py" rồi chạy
- [x] :tada: **Linux:**
```
pyuic5 -x file.ui -o file.py 
```
- [x] :tada: **Windows:**
```
python -m PyQt5.uic.pyuic -x file.ui -o file.py
```

# Cài đặt Pyqt5
```
$ pip3 install pyqt5                                                      (Thư viện)
$ pip3 install qyqt5 tools                                                (Thư viện chuyển đuôi .ui sang .py)
$ pip3 install pyqt5designer                                              (Phần mềm thiết kế QtDesigner)
```

# 1. Chuyển đuôi ".ui" thành ".py"
- [x] :tada: **Linux:**
```
pyuic5 -x file.ui -o file.py 
```
- [x] :tada: **Windows:**
```
python -m PyQt5.uic.pyuic -x file.ui -o file.py
```

# 2. Chuyển đuôi ".py" thành ".exe"
#### Cài Đặt
```
$ pip3 install pyinstaller                                                (Thư viện chuyển đuôi .py thành .exe)
```

***Note:*** **-w** "off console window",  **-y** "need to continuous integration"
- [x] :tada: **Linux:**
```
$ pyinstaller --onefile -w -y file.py 
$ pyinstaller --onefile -w file.py
```

- [x] :tada: **Windows:**
```
python -m PyInstaller --onefile -w file.py
```
