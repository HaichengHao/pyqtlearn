
'''
您可以使用 .setContentMargins
设置布局周围的间距，或使用 .setSpacing 设置元素之间的间距。
'''

import sys
from PyQt6.QtWidgets import QWidget,QApplication,QMainWindow,QVBoxLayout,QHBoxLayout
from layout_colorwidget import Color


class mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')

        #设置layout
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout1.setContentsMargins(0,0,0,0)
        layout1.setSpacing(3)

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('blue'))

        layout1.addLayout(layout2)
        layout1.addWidget(Color('purple'))

        layout3.addWidget(Color('orange'))
        layout3.addWidget(Color('yellow'))
        layout3.addWidget(Color('green'))

        layout1.addLayout(layout3)

        #创建主要容器
        container = QWidget()
        container.setLayout(layout1)

        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = mainWindow()
window.show()

app.exec()
