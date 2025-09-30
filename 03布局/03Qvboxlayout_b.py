import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')

        #创建布局
        layout = QVBoxLayout()

        #给布局中添加组件
        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))


        #创建容器组件
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window =MainWindow()

window.show()

app.exec()