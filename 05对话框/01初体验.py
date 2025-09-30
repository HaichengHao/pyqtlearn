#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pyqtlearn 
@File    ：01初体验.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/9/29 16:45 
'''

'''
在 Qt 中，对话框由 QDialog 类处理。
要创建一个新的对话框只需创建一个 QDialog 类型的对象，
并将其父控件（例如QMainWindow）作为其父对象传递给该对象即可。

让我们创建自己的 QDialog。首先，我们从一个简单的框架应用程序开始，
该应用程序有一个按钮，该按钮与槽方法相连。'''

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QDialog, QPushButton

)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')

        button = QPushButton('点我出对话框')
        button.clicked.connect(self.btn_clicked)
        self.setCentralWidget(button)

    def btn_clicked(self, s):
        print(s)
        dlg = QDialog(self)
        dlg.setWindowTitle('小飞棍来咯')
        dlg.exec()

'''
在槽 button_clicked（接收按钮按下的信号）中，
我们创建对话框实例，并将我们的 QMainWindow 实例作为父窗口传递。
这将使对话框成为 QMainWindow 的模态窗口。这意味着对话框将完全阻止与父窗口的交互。
一旦创建了对话框，我们使用 exec() 函数启动它——就像我们之前使用 QApplication 创建应用程序的主事件循环一样。
这并非巧合：当您执行 QDialog 时，会为对话框专门创建一个全新的事件循环。
'''


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
'''
一个事件循环统领一切

还记得我提到过，任何时候只能有一个 Qt 事件循环在运行吗？我是认真的！QDialog 会完全阻塞你的应用程序执行。
不要在启动对话框的同时，还期望应用程序的其他部分继续运行。

我们稍后将探讨如何利用多线程技术来解决这一难题'''
