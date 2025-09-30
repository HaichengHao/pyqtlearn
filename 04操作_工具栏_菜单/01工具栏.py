'''
接下来，我们将探讨一些常见的用户界面元素，这些元素您可能在许多其他应用程序中都见过——工具栏和菜单。
我们还将探索Qt提供的用于减少不同用户界面区域之间重复性的便捷系统—— QAction。
'''
'''
工具栏
最常见的用户界面元素之一是工具栏。工具栏是由图标和/或文本组成的条形控件，
用于在应用程序中执行常见任务，而通过菜单访问这些任务会显得繁琐。
它们是许多应用程序中最为常见的用户界面功能之一。尽管一些复杂的应用程序，
特别是微软Office套件中的应用程序，已迁移到基于上下文的“功能区”界面，
但对于您将创建的大多数应用程序而言，标准工具栏已足够使用。
Qt 工具栏支持显示图标、文本，还可以包含任何标准的 Qt 控件。
但是，对于按钮而言，最好的方法是利用 QAction 系统将按钮放置在工具栏上'''



import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QToolBar, QMainWindow, QLabel, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')

        label = QLabel("hello")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        toolbar = QToolBar('主工具栏')
        self.addToolBar(toolbar)

    def onMyToolBarButtonClicked(self,s):
        print("click",s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

# 一旦您移除了工具栏，现在就没有地方可以右键点击来重新添加它
# 因此，作为一个通用的规则，您应该要么保留一个不可移除的工具栏，要么提供一个替代界面来开启或关闭工具栏。