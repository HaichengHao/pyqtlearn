'''
接下来，我们将把 QAction 设置为可切换的——点击一次会将其打开，再次点击会将其关闭。
要实现这一点，我们只需在 QAction 对象上调用 setCheckable(True) 方法。
'''
import sys
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QToolBar,
    QStatusBar
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        self.label = QLabel("O(∩_∩)O哈哈~")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(self.label)

        toolbar = QToolBar()
        self.addToolBar(toolbar)
        btn_action = QAction("点击", self)
        btn_action.setCheckable(True)  # important：这是当前要关注的点
        btn_action.setStatusTip("点击看变化")
        btn_action.triggered.connect(self.btn_triggered)
        toolbar.addAction(btn_action)

        self.setStatusBar(QStatusBar(self))

    def btn_triggered(self, s):
        if s == True:
            self.label.setText("(#^.^#)")
            print("a",s)
        else:
            self.label.setText("oiiaiioiia")
            print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
