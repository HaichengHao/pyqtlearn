import os
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap

basedir = os.path.dirname(__file__)
print(basedir)  # 获取当前文件所在的文件夹

print('当前活动目录', os.getcwd())
print(f'路径与{basedir}相关')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('vimin')
        widget = QLabel("(*´▽｀)ノノ")
        widget.setPixmap(QPixmap(os.path.join(basedir, "monkyking.png")))
        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

'''
如果您现在运行这个脚本，图像将如预期显示——无论您从哪里运行脚本。
脚本还会输出路径（以及当前工作目录），以帮助调试问题。
在从应用程序加载任何外部文件时，请务必记住这一点。
'''