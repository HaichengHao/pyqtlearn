import sys
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        self.setFixedSize(QSize(800,600))
        button = QPushButton('点击我')
        button.setCheckable(True) #设置点击就会高亮
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)
        button.setFixedSize(QSize(100,100))

        self.setCentralWidget(button)
    def the_button_was_clicked(self):
        print('按钮被点击了')
    def the_button_was_toggled(self,checked):
        print('按钮激活了?',checked)
    '''
    您可以将任意数量的槽连接到一个信号，并可以在槽上同时响应不同版本的信号
    '''

APP=QApplication(sys.argv)
window=MainWindow()
window.show()

APP.exec()
