'''
让我们让工具栏变得更有趣一些。我们只需添加一个 QButton 控件即可，
但 Qt 中还有一种更好的方法可以为您提供一些很酷的功能——那就是通过 QAction。
QAction 是一个提供描述抽象用户界面的方法的类。这意味着，您可以在一个对象中定义多个界面元素，
并通过与该元素交互的效果将它们统一起来。例如，工具栏和菜单中通常都会出现一些功能，例如“编辑→剪切”，
它既存在于“编辑”菜单中，也以剪刀图标的形式出现在工具栏上，同时还支持键盘快捷键 Ctrl-X（macOS 上为 Cmd-X）
'''
from PyQt6.QtGui import QAction

'''
如果没有 QAction，您必须在多个地方定义此操作。但使用 QAction ，您就可以只定义一个 QAction，定义触发操作，然后将此操作添加到菜单和工具栏中。每个 QAction 都有名称、状态消息、图标和可连接的信号（以及更多内容）。

请参阅下面的代码，了解如何添加您的第一个 QAction'''

from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QToolBar, QLabel
import sys
from PyQt6.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        label = QLabel("(*´▽｀)ノノ")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)

        # step 1:设置工具栏,并在主窗口上添加工具栏
        toolbar = QToolBar("主工具栏")
        self.addToolBar(toolbar)

        """ 
        下面这个是QAction.py的源码注释，这里使用的是条例2,一个字符串，一个父对象，self就是我们的MainWindow
            QAction(parent: Optional[QObject] = None)
            QAction(text: Optional[str], parent: Optional[QObject] = None)
            QAction(icon: QIcon, text: Optional[str], parent: Optional[QObject] = None)
            """

        '''
        首先，我们创建一个函数来接受来自 QAction 的信号，以便查看它是否正常工作。
        接下来，我们定义 QAction 本身。
        在创建实例时，我们可以传递一个动作标签和/或图标。
        你还必须传递任何 QObject 作为动作的父对象——这里我们传递 self 作为对主窗口的引用。
        对于 QAction 来说，父对象作为最后一个参数传递，这有点奇怪。
        接下来，我们可以选择设置一个状态提示——一旦有状态栏，该文本就会显示在状态栏上。
        最后，我们将 .triggered 信号连接到自定义函数。每当 QAction 被“触发”（或激活）时，该信号就会触发。'''
        button_action = QAction("你的按钮", self)
        button_action.setStatusTip("这是你的按钮!!!!!!!")

        button_action.triggered.connect(self.onMyToolBarButtonClick)

        toolbar.addAction(button_action)  # 给工具栏添加action

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = QApplication(sys.argv)
window = MyWindow()
window.show()

app.exec()

'''
为什么信号总是为假？

传递的信号表明该操作是否被选中，
而由于我们的按钮不能被选中——只能点击——因此它总是为假。这就像我们之前看到的 QPushButton 一样
'''
