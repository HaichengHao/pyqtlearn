import sys
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import QMainWindow,QApplication,QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        button = QPushButton('点击我')
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        #设置窗口的中心控件
        self.setCentralWidget(button)
        self.setFixedSize(QSize(500,400))

    def the_button_was_clicked(self):
        print('按钮被触发')

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()