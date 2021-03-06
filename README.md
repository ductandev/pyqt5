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
-x : execu (thực thi) \
-o : output
- [x] :tada: **Windows:**
```
python -m PyQt5.uic.pyuic -x file.ui -o file.py
```

# Cài đặt Pyqt5
```
$ pip3 install pyqt5                                                      (Thư viện)
$ pip3 install pyqt5-tools                                                (Thư viện chuyển đuôi .ui sang .py)
$ pip3 install pyqt5designer                                              (Cho windows Phần mềm thiết kế QtDesigner)

Cài pyQt5 Designer for linux
$ sudo apt-get install qttools5-dev-tools                                 
$ sudo apt-get install qttools5-dev
$ sudo apt-get install python3-pyqt5
$ sudo apt-get install qtcreator pyqt5-dev-tools
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

***Note:*** **-w** "Không hiển thị cửa sổ console windows",  **-y** "need to continuous integration", **--onefile** : đóng gói tất cả vào 1 file duy nhất nên sẽ không biết thiếu file gì
```
+ Đóng gói chương trình vào một file duy nhất:
$ pyinstaller -F test.py 

Sau quá trình đóng gói, bên trong thư mục dist sẽ xuất hiện “stand-alone executable file” test.exe, file này sẽ có dung lượng khá lớn vì nó chứa cả các thư viện liên quan.

+ Đóng gói chương trình cùng với icon file (tạo icon cho file):
$ pyinstaller -i programIcon.ico test.py
$ python -m PyInstaller --onefile -w --icon=d:\Share_ubuntu\Lay_anh_opencv-main\Bai4\2.ico .\main_new.py

Trong đó: programIcon.ico là icon file.
```
Tạo icon from giao diện : https://www.geeksforgeeks.org/how-to-set-icon-to-a-window-in-pyqt5/# \
Video hướng dẫn tạo icon bằng pyInstaller: https://www.youtube.com/watch?v=bV8nB5jEid4 \
Trang convert .png sang đuôi .ico : https://www.icoconverter.com/

- [x] :tada: **Linux:**
```
$ pyinstaller --onefile -w -y file.py 
$ pyinstaller --onefile -w file.py
```

- [x] :tada: **Windows:**
```
python -m PyInstaller --onefile -w file.py
```
