import sys
from PyQt6.QtCore import QSize,Qt

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton
)

# 创建子类 QMainWindow 来自定义您的应用程序的主窗口
'''
常用的 Qt 控件总是从 QtWidgets 命名空间导入。
我们必须始终调用 super() 类的 __init__方法。
使用 .setCentralWidget 在 QMainWindow 中放置一个控件。
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('VIMIN')
        button = QPushButton('点击我')

        #设置窗口的中心控件
        self.setCentralWidget(button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
'''
在我们的 __init__ 块中，我们首先使用 .setWindowTitle() 来更改我们主窗口的标题。 然后，我们将第一个窗口控件——一个 QPushButton 添加到窗口中间。这是 Qt 中可用的基本部件之一。 在创建按钮时，您可以输入希望按钮显示的文本。

最后，我们在窗口上调用 .setCentralWidget()。 这是 QMainWindow 特有的函数，用于设置窗口中间的控件。
'''