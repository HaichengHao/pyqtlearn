'''
到目前为止，我们已经看到了将控件信号连接到 Python 方法的示例。当控件触发信号时，我们的 Python 方法会被调用，并接收来自信号的数据。
但您并不总是需要使用 Python 函数来处理信号——您也可以将 Qt 控件直接相互连接。

在下面的示例中，我们将一个 QLineEdit 控件和一个 QLabel 添加到窗口中。
在窗口的 __init__ 中，我们将我们的行编辑 .textChanged 信号连接到 QLabel 上的 .setText 方法。现在，每当 QLineEdit 中的文本发生更改时，
QLabel 都会将该文本发送到其 .setText 方法。
'''

from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QLabel,QLineEdit,QVBoxLayout,
    QWidget
)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel() #不能互动的标签
        self.input = QLineEdit() #输入一行文本
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input) #tips:注意添加的都是带括号的!!!
        layout.addWidget(self.label)

        # ✅ 创建一个容器 widget 为中央容器
        container = QWidget()
        # ✅ 将布局设置给容器
        container.setLayout(layout) #将layout设置为这个容器的布局
        # ✅ 将容器设置为窗口的中央控件
        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

