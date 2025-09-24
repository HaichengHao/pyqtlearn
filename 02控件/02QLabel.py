'''
我们将从 QLabel 开始介绍，
它可以说是 Qt 工具箱中最简单的控件之一。
这是一个简单的单行文本，您可以将其放置在应用程序中。
您可以在创建时通过传递字符串来设置文本
'''

import sys
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import QApplication,QWidget,QLabel,QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Vimin')

        widget = QLabel('我就是个无法编辑的文字信息！！！')
        font = widget.font() #利用widget.font()获取当前字体，对其进行修改然后将其应用回去,这样可以确保字体与系统字体样式保持一致

        widget.setFont(font)
        widget.setAlignment(
            # Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignVCenter
            Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignBottom
        )#对齐方式通过Qt.命名空间中的标志来指定,本次使用的是水平方向和垂直方向居中对齐
        # 您可以使用管道符（|）将多个标志组合在一起，但请注意，每次只能使用一个垂直或水平对齐标志。
        '''
        请注意，您使用了或运算符 (|) 按照惯例将两个标志组合在一起。
        这些标志是非重叠的位掩码。例如，Qt.AlignmentFlag.AlignLeft 的二进制值为 0b0001，
        而Qt.AlignmentFlag.AlignBottom 的二进制值为 0b0100。
        通过按位或运算，我们得到值 0b0101，表示“底部左侧”。'''

        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()

window.show()

app.exec()


