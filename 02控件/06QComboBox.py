'''
QComboBox 是一个下拉列表，默认情况下处于关闭状态，需要点击箭头才能打开。您可以从列表中选择一个项目，
当前选中的项目将作为标签显示在控件上。组合框适用于从长列表中选择一个选项。
'''
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication,QMainWindow,QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('VIMIN')

        widget = QComboBox()
        #tips:QComboBox 也可以设置为可编辑模式，允许用户输入列表中不存在的值，并可选择将这些值插入列表或直接作为选中项使用
        widget.setEditable(True)
        widget.addItems(['simin','min','mm336441'])
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        '''
        当当前选中的项目被更新时，会触发 .currentIndexChanged 信号，默认情况下会传递列表中选中项目的索引。
        还有一个 .currentTextChanged 信号，它提供当前选中项目的标签，这个通常会更加实用。'''
        self.setCentralWidget(widget)

    def index_changed(self,i): #i这是一个int型整数，接受的是信号currendIndexChanged
        print(i)
    def text_changed(self,s): #s是一个str类型的字符串
        print(s)


app = QApplication(sys.argv)
window =MainWindow()
window.show()
app.exec()