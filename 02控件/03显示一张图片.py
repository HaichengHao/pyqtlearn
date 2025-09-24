'''
有趣的是，您也可以使用 QLabel 通过 .setPixmap() 方法显示一张图片。
该方法接受一个像素图（像素数组），您可以通过将图片文件名传递给 QPixmap 来创建它。
在随本书提供的示例文件中，您可以找到一个名为 otje.jpg 的文件(这里就用自己的)，
您可以按照以下方式在窗口中显示它：
'''

import sys
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt6.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Vimin')
        widget = QLabel('泥嚎!')
        widget.setPixmap(QPixmap('monkyking.png'))
        widget.setFixedSize(QSize(400,400))
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()

window.show()

app.exec()
