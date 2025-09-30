'''


我们将介绍的最后一种布局是 QStackedLayout。
如上所述，这种布局允许您将元素直接放置在彼此前面。
然后，您可以选择要显示的控件。您可以在图形应用程序中使用它来绘制图层，
或模仿标签式界面。请注意，还有 QStackedWidget，这是一个完全以相同方式工作的容器控件。
如果您希望直接将一个栈添加到 QMainWindow 中，可以使用 .setCentralWidget 方法

'''

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QMainWindow,
    QStackedLayout
)
from layout_colorwidget import Color

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')

        layout = QStackedLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('yellow'))
        layout.addWidget(Color('putple'))

        layout.setCurrentIndex(3) #tips:这里按照列表那样的索引排序,所以显示的是黄颜色的界面

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
'''
QStackedWidget 是应用程序中标签视图的工作方式。
任何时候只能看到一个视图（“标签”）。
您可以随时使用 .setCurrentIndex() 或 .setCurrentWidget() 通过索引（按控件添加的顺序）
或控件本身来设置项目，从而控制要显示的控件。'''