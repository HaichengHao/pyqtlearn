'''
首先，让我们使用新创建的“颜色”控件将整个窗口填充为单一颜色来测试这个控件。
完成之后，我们可以使用
 .setCentralWidget 将它添加到主窗口，这样就得到了一个纯红色的窗口。
'''

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        widget = Color('red')
        self.setCentralWidget(widget)

app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()
'''
接下来，我们将依次查看所有可用的 Qt 布局。请注意，要将布局添加到窗口中，我们需要一个占位 QWidget 来容纳布局
'''