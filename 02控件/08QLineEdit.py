'''
QLineEdit 控件是一个简单的单行文本编辑框，
用户可以在其中输入内容。这些控件用于表单字段或没有限制有效输入列表的设置。
例如，输入电子邮件地址或计算机名称时。
'''

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        widget = QLineEdit()
        widget.setMaxLength(10)#tips:可以通过使用 .setMaxLength 方法为文本字段设置最大长度
        widget.setPlaceholderText("输入文字")
        #tips:占位符文本（即在用户输入内容前显示的文本）可通过 .setPlaceholderText 方法添加

        # widget.setReadOnly(True) 设置为只读模式

        widget.returnPressed.connect(self.return_pressed) #tips:按下回车键时
        widget.selectionChanged.connect(self.selection_changed)#tips:选择更改时
        widget.textChanged.connect(self.text_changed) #tips:文本被更改时
        widget.textEdited.connect(self.text_edited) #tips:文本被编辑时

        self.setCentralWidget(widget)

    def return_pressed(self):
        print('回车键被按下')
        self.centralWidget().setText('boom!!!')

    def selection_changed(self):
        print('选择更改') #tips:就是按住划选一块儿要更改的文字
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print('文字改变了')
        print(s)

    def text_edited(self, s):
        print('文字被编辑了!!')
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
