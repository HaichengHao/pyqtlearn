'''
通常，将控件的当前状态存储在 Python 变量中非常有用。
这样就可以像处理其他 Python 变量一样处理这些值而无需访问原始控件。
您可以将这些值存储为单独的变量，或者根据需要使用字典。在下一个示例中，
我们将按钮的选中值存储在名为 button_is_checked 的变量中。

Listing 8. basic/signals_and_slots_1c.py
'''

import sys
from PyQt6.QtCore import Qt, QSize

from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_is_checked = False  # 默认是不被点选，注意这个变量是自己声明的
        self.setWindowTitle('vimin')
        self.setFixedSize(QSize(800, 800))
        button = QPushButton('点击我')
        button.setCheckable(True)

        #设置一个绑定信号the_button_was_toggled
        button.clicked.connect(self.the_button_was_toggled)

        button.setChecked(self.button_is_checked)  # 使用默认值设置控件的初始状态
        self.setCentralWidget(button)

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked  # 当控件状态发生变化时,更新变量以匹配
        print(self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
