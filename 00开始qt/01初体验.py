from PyQt6.QtWidgets import QApplication,QWidget

import sys

# 每个应用程序需要一个（且只有一个）QApplication 实例
# 输入 sys.argv，这可以允许应用程序使用命令行参数
# 如果知道不会使用命令行参数,也可以使用 QApplication([])

# tips:创建一个QApplication 实例，传入 sys.arg
app = QApplication(sys.argv)
'''
如果您不会使用命令行参数来控制 Qt，您可以传递一个空列表，例如
app = QApplication([])
'''

#创建一个Qt widget作为我们的窗口

window = QWidget()
window.show()

#开始时间循环
app.exec()

