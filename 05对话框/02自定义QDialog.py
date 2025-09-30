#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pyqtlearn 
@File    ：02自定义QDialog.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/9/29 16:54 
'''
'''
就像我们的第一个窗口一样，这个窗口也不太有趣。
让我们通过添加一个对话框标题和一组“确定”和“取消”按钮来解决这个问题，
以便用户可以接受或拒绝该模态窗口。

要自定义 QDialog，我们可以继承它。'''

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QLabel, QMenu, QPushButton, QDialogButtonBox, \
    QVBoxLayout
import sys


# tips:自定义一个对话框
class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
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

    def btn_clicked(self, s):
        dlg = CustomDialog()
        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()
'''
在上述代码中，我们首先创建了 QDialog 的子类，并将其命名为 CustomDialog 。
对于 QMainWindow，我们在类中的 __init__ 块中应用自定义设置，
以便在对象创建时应用这些自定义设置。
首先，我们使用 .setWindowTitle() 为 QDialog 设置标题，与我们为主窗口设置标题的方式完全相同。'''