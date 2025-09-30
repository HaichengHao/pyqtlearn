#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pyqtlearn 
@File    ：10标准的QmessageBox对话框.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/9/30 11:51 
'''
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction

'''
为了进一步简化操作，QMessageBox 还提供了一系列静态方法，
这些方法可用于直接显示此类消息对话框，而无需先创建 QMessageBox 实例。这些方法如下所示：
QMessageBox.about(parent, title, message)
QMessageBox.critical(parent, title, message)
QMessageBox.information(parent, title, message)
QMessageBox.question(parent, title, message)
QMessageBox.warning(parent, title, message)
'''
# parent 参数是对话框所属的父窗口。如果您是从主窗口启动对话框，
# 可以使用 self 引用主窗口对象。以下示例创建一个问题对话框，与之前示例类似，包含“是”和“否”按钮

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QMessageBox, QMenu, QMenuBar
)
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        self.label = QLabel("(*´▽｀)ノノ")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(self.label)

        menu = self.menuBar()  # 设置菜单栏

        # 往菜单栏里加入条目
        file_menu = menu.addMenu("&files")

        btn = QAction("点我", self)
        btn.triggered.connect(self.btn_clicked)
        btn2 = QAction("点我", self)
        # btn.setShortcut()
        file_menu.addAction(btn)

        file_menu.addSeparator()

        sub_menu = file_menu.addMenu("submenu")
        sub_menu.addAction(btn2)

        optionmenu = menu.addMenu("optionmenu")

    def btn_clicked(self, s):
        button = QMessageBox.question(
            self, "问题对话框", "问题信息"
        )
        if button == QMessageBox.StandardButton.Yes:
            print('yes')
        else:
            print('no')


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec()
