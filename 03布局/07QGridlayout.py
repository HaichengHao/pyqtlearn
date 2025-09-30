'''
尽管它们非常有用，但如果您尝试使用 QVBoxLayout 和 QHBoxLayout 来布局多个元素（例如表单）
，您会发现很难确保不同大小的控件对齐。解决此问题的办法是使用 QGridLayout
'''

import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QGridLayout,QLabel
from layout_colorwidget import Color
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        layout = QGridLayout()

        layout.addWidget(Color('red'),0,0)
        layout.addWidget(Color('green'),1,1)
        layout.addWidget(Color('blue'),2,2)
        layout.addWidget(Color('purple'),3,3)

        container = QWidget()
        container.setLayout(layout)
        container.setFixedSize(QSize(800,800))
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()


