#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pyqtlearn 
@File    ：03带parent的QDialog.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/9/29 18:29 
'''

'''
当您点击按钮以启动对话框时，可能会发现它出现在父窗口之外——通常位于屏幕中央。
通常您希望对话框出现在其启动窗口之上，以便用户更容易找到。要实现这一点，
我们需要为对话框指定一个父窗口。
如果我们将主窗口作为父窗口传递给 Qt，Qt 会将新对话框的位置调整为对话框的中心与窗口的中心对齐。

我们可以修改我们的 CustomDialog 类，使其接受一个 parent 参数。
'''

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QLabel, QMenu, QPushButton, QDialogButtonBox, \
    QVBoxLayout
import sys


# tips:自定义一个对话框
class CustomDialog(QDialog):
    def __init__(self,parent=None): #step 1:设定一个带parent的实例属性
        super().__init__(parent)
        self.setWindowTitle('(*´▽｀)ノノ')
        buttons = (
                QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("出现了一些问题，还好吗?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')

        btn = QPushButton('点我看效果')
        btn.setStatusTip("点我出弹窗")
        btn.clicked.connect(self.btn_clicked)

        self.setCentralWidget(btn)


    #step 2:
    '''
    然后，当我们创建自定义对话框的实例时，可以将主窗口作为参数传递进去。
    在我们的 button_clicked 方法中，self 就是我们的主窗口对象。'''
    def btn_clicked(self, s):
        dlg = CustomDialog(self)
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()