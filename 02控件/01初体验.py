'''
在 Qt 中，控件是指用户可以与之交互的用户界面（UI）组件。用户界面由多个控件组成，这些控件被排列在窗口内。Qt 提供了大量可用的控件，甚至允许您创建自己的自定义控件。

在本书的代码示例中，有一个名为 basic/widgets_list.py 的文件，您可以运行它来在窗口中显示一组控件。它使用了一些我们稍后会介绍的复杂技巧，所以，现在先不要担心代码的问题

'''
import sys

from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,  # <2>
    QWidget,  # <1>
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        layout = QVBoxLayout() #tips：创建一个布局
        widgets = [
            QCheckBox, #复选框
            QComboBox, #下拉列表框
            QDateEdit,
            QDateTimeEdit,
            QDial,#可旋转表盘
            QDoubleSpinBox, #浮点数微调框
            QFontComboBox,
            QLCDNumber,
            QLabel,#不能互动的标签
            QLineEdit,#输入一行文本
            QProgressBar, #进度条
            QPushButton,
            QRadioButton,#仅有一个有效选项的选项组
            QSlider,#滑块
            QSpinBox,#整数微调框
            QTimeEdit,
        ]

        for w in widgets:
            layout.addWidget(w()) #important:注意这里添加的是带括号的!!

        widget = QWidget() #tips:创建一个主组件容器
        widget.setLayout(layout) #tips:然后把布局添加到这个组件容器上面去

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget) #设置主的组件容器为窗口的中央控件


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
