'''
让我们添加一个状态栏。

我们通过调用 QStatusBar 并将其结果传递给 .setStatusBar 来创建状态栏对象。
由于我们不需要修改状态栏设置，因此可以在创建时直接将其传递进去。我们可以在一行代码中创建并定义状态栏：
'''
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QMainWindow, QToolBar, QStatusBar
)
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        self.label = QLabel("Hi~ o(*￣▽￣*)ブ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(self.label)

        toolbar = QToolBar("工具栏")
        self.addToolBar(toolbar)  #tips:让窗口添加上toolbar

        button_action = QAction("点我",self)
        button_action.setStatusTip("点我变好看")

        button_action.triggered.connect(self.btn_triggered)

        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self)) #important:给自己加一个状态栏

    def btn_triggered(self,s):
        self.label.setText("oiiaio")
        print(s)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

