import os.path

from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QLabel, QToolBar, QStatusBar
)
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt, QSize
import sys

basedir = os.path.dirname(__file__)
print(basedir)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        self.label = QLabel("点我")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(self.label)

        toolbar = QToolBar()
        self.addToolBar(toolbar)

        button_action = QAction(QIcon(os.path.join(basedir, 'bug.png')), "点击我", self)
        button_action.setStatusTip("我是一条提示")
        button_action.setCheckable(True)
        button_action.triggered.connect(self.onmyToolbarclick)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onmyToolbarclick(self, s):
        print(s)
        if s == True:
            self.label.setText("oiiaiioiia")
        else:
            self.label.setText("😂😂😂")

app = QApplication(
    sys.argv
)
window = MainWindow()
window.show()
app.exec()
