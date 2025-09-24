import sys
from PyQt6.QtCore import QSize,Qt
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        button = QPushButton('点我')
        #设置固定的大小,注意这样设置之后是不能够拖动的
        self.setFixedSize(QSize(400,300))
        '''
        除了可以调用 .setFixedSize() 方法外，您还可以调用 .setMinimumSize() 和.setMaximumSize() 方法分别设置窗口的最小和最大尺寸。您不妨亲自尝试一下！
        '''
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

