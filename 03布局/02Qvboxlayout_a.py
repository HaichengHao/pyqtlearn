import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')

        layout = QVBoxLayout()  # 创建一个垂直布局
        layout.addWidget(Color('red'))  # 往布局内塞入控件

        widget = QWidget()  # 创建一个大组件作为容器
        widget.setLayout(layout) #然后给这个大组件里塞入布局

        self.setCentralWidget(widget)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
