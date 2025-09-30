'''
Qt 提供了一个内置的选项卡控件，可以提供09那种布局，非常方便——尽管它实际上是一个控件，
而不是一个布局。下面的选项卡演示是使用 QTabWidget 重新创建的
'''

import sys
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QTabWidget,
    QWidget
)
from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        self.setMinimumSize(400,400)
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.East)  # 这里指定位置很有意思,是东西南北
        tabs.setMovable(True)
        for n, color in enumerate(['red', 'blue', 'green', 'yellow']):
            tabs.addTab(Color(color), color)  # 第一个参数是tab对象(其实就是组件),第二个是tab的文字
        self.setCentralWidget(tabs)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
