import sys
from layout_colorwidget import Color
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('混合布局')

        #设置布局
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        #在布局1中添加布局2
        layout1.addLayout(layout2)
        #然后横向布局再加一个green
        layout1.addWidget(Color('green'))

        #在布局3中添加组件
        layout3.addWidget(Color('blue'))
        layout3.addWidget(Color('yellow'))


        #然后把布局1中添加布局3
        layout1.addLayout(layout3)

        #创建容器组件
        container = QWidget()
        container.setLayout(layout1)
        self.setCentralWidget(container)

app = QApplication(
    sys.argv
)

window = MainWindow()
window.show()

app.exec()

