'''
QListWidget。该控件与 QComboBox 类似，
只是选项以可滚动列表的形式呈现。它还支持同时选择多个项目。
QListWidget 提供了一个 currentItemChanged 信号，
该信号发送 QListItem（列表控件的元素），以及一个 currentTextChanged 信号，
该信号发送当前项目的文本。
'''

from PyQt6.QtWidgets import QApplication, QMainWindow, QListWidget
import sys
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        self.setWindowIcon(QIcon('monkyking.png'))
        widget = QListWidget()
        widget.addItems(['simin', 'min', 'mm336'])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):  # 不是索引，i 是 QListItem
        print(i)

    def text_changed(self, s):
        print(s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()