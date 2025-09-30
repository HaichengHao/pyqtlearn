#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pyqtlearn 
@File    ：04QMessageBox.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/9/29 20:03 
'''
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QLabel, QMessageBox, QPushButton, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        btn = QPushButton('点我')
        btn.clicked.connect(self.button_clicked)
        self.setCentralWidget(btn)

    def button_clicked(self, is_checked):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("我有一个疑问!!")
        dlg.setText("这是一个简单的对话框")
        btn = dlg.exec()
        #tips：查找按钮枚举项并获取结果
        btn = QMessageBox.StandardButton(btn)

        if btn == QMessageBox.StandardButton.Ok:
            print("ok!!!!")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
