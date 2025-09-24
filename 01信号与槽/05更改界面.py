'''
到目前为止，我们已经了解了如何接受信号并将输出打印到控制台。
但是，当我们点击按钮时，如何在界面中触发某些操作呢？让我们更新槽方法来修改按钮，
更改文本并禁用按钮，使其不再可点击。我们还将暂时删除可选状态。
'''

import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication,QMainWindow,QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        self.button = QPushButton('点击我')
        self.button.clicked.connect(self.the_button_was_clicked)

        #设置窗口的中心控件
        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        #tips:您可以通过向 .setText() 方法传递一个字符串来更改按钮的文本

        self.button.setText('你已经点过我了')
        self.button.setEnabled(False) #tips:要禁用按钮，请调用 .setEnabled() 方法并传入 False


        #我们也来更改窗口标题
        self.setWindowTitle("mylove")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
