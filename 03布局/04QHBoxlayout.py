'''
要使用它，我们可以简单地将 QVBoxLayout 改为 QHBoxLayout。现在，这些框会从左到右排列
'''

import sys
from layout_colorwidget import Color
from PyQt6.QtWidgets import QWidget,QApplication,QMainWindow,QHBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')

        layout = QHBoxLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
