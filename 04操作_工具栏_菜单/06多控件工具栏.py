from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtWidgets import (
    QWidget, QLabel, QMainWindow, QToolBar, QStatusBar, QApplication, QCheckBox
)
import sys
import os

basedir = os.path.dirname(__file__)
print(basedir)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')

        self.label = QLabel('(*´▽｀)ノノ')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(self.label)

        action_button1 = QAction(QIcon(os.path.join(basedir, 'bug.png')), '调试按钮', self)
        action_button1.setCheckable(True)
        action_button1.setStatusTip("点我调试")
        # action_button1.triggered.connect()

        action_button2 = QAction('点击我', self)
        action_button2.setCheckable(True)
        action_button2.setStatusTip("点我试试")

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        toolbar.addAction(action_button1)
        toolbar.addAction(action_button2)

        toolbar.addWidget(QLabel("新组件"))
        toolbar.addWidget(QCheckBox())
        self.setStatusBar(QStatusBar(self))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
