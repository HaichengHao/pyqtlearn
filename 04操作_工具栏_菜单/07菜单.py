'''
要创建菜单，我们需要在 QMainWindow 上调用 .menuBar() 方法来创建菜单栏。
我们通过调用 .addMenu() 方法并传入菜单名称来在菜单栏上添加菜单。
我将其命名为 ‘&File’。这里的 & 符号定义了快捷键，按下 Alt 键时可快速跳转到该菜单
'''
import os

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QWidget, QLabel, QMainWindow, QToolBar, QStatusBar, QApplication
)
import sys
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt

basedir = os.path.abspath(os.path.dirname(__file__))
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        label = QLabel('你好')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)

        toolbar = QToolBar("主工具栏")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        button_action = QAction(
            QIcon(os.path.join(basedir,'bug.png')),
            "&按钮",
            self
        )
        button_action.setStatusTip("点我看bug")
        # button_action.triggered.connect()
        button_action.setCheckable(True)

        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(
            "&按钮2",
            self
        )
        button_action2.setStatusTip("你的第二个按钮")
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        self.setStatusBar(QStatusBar(self))

        #定义菜单栏
        menu = self.menuBar()
        #给菜单栏加上菜单
        file_menu = menu.addMenu("&file")
        file_menu.addAction(button_action)
        file_menu.addSeparator() #tips:给菜单添加一条分隔符
        file_menu.addAction(button_action2)
        # tips:点击菜单中的选项时，您会发现该选项可切换状态——它继承了 QAction 的特性。

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()



