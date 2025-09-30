#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pyqtlearn 
@File    ：05QMessageBox2.py
@IDE     ：PyCharm 
@Author  ：百年
@Date    ：2025/9/29 20:34 
'''
import sys

from PyQt6.QtGui import QAction

'''
与我们之前讨论的对话框按钮框类似， QMessageBox 上显示的按钮也通过一组常量进行配置，
这些常量可以使用 | 符号组合以显示多个按钮。
QMessageBox.Ok
QMessageBox.Open
QMessageBox.Save
QMessageBox.Cancel
QMessageBox.Close
QMessageBox.Discard
QMessageBox.Apply
QMessageBox.Reset
QMessageBox.RestoreDefaults
QMessageBox.Help
QMessageBox.SaveAll
QMessageBox.Yes
QMessageBox.YesToAll
QMessageBox.No
QMessageBox.NoToAll
QMessageBox.Abort
QMessageBox.Retry
QMessageBox.Ignore
QMessageBox.NoButton


您还可以通过设置以下其中一个图标来调整对话框中显示的图标：

Table 3. QMessageBox icon constants.

图标状态	Description
QMessageBox.NoIcon	消息框没有图标
QMessageBox.Question	这条消息是在提问
QMessageBox.Information	该信息仅供参考
QMessageBox.Warning	该消息为警告信息
QMessageBox.Critical	该消息表明存在一个严重问题
'''

# tips:例如，以下代码创建一个带有“是”和“否”按钮的对话框。


from PyQt6.QtWidgets import QMessageBox, QPushButton, QMainWindow, QApplication, QDialog, QToolBar, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        self.label = QLabel("哈哈")
        tool_bar = QToolBar()

        self.addToolBar(tool_bar)
        btn = QAction("点我",self)
        btn.setStatusTip("点我弹窗口")
        btn.triggered.connect(self.button_clicked)
        tool_bar.addAction(btn)
        self.setCentralWidget(self.label)


    def button_clicked(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("确定操作")
        dlg.setText("你确定吗?")
        dlg.setStandardButtons(
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No
        )
        dlg.setIcon(QMessageBox.Icon.Question)
        result = dlg.exec()
        print(result)

        if result == QMessageBox.StandardButton.Yes:
            print('yes!!')
        else:
            print('no!!')


app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
app.exec()
