'''
QSlider 提供了一个滑动条控件，其内部功能与 QDoubleSpinBox 非常相似。
它不会以数字形式显示当前值，而是通过滑块在控件长度上的位置来表示。
当需要在两个极端值之间进行调整，但不需要绝对精确度时，此控件非常有用。此类控件最常见的用途是音量控制。

还有一个额外的每当滑块移动位置时触发的 .sliderMoved 信号，
以及一个每当滑块被点击时发出的 .sliderPressed 信号。
'''

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QSlider,QApplication


class myWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        widget = QSlider(Qt.Orientation.Horizontal)

        #您还可以通过在创建时传递方向来构建垂直或水平方向的滑块。方向标志在 Qt.命名空间中定义
        # widget.QSlider(Qt.Orientation.Horizontal)
        # 或者widget.QSlider(Qt.Orientiation.Vertical)

        widget.setMaximum(3)
        widget.setMinimum(-10)

        widget.setSingleStep(3)
        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self,i):
        print('发生变化',i)

    def slider_position(self,p):
        print('位置',p)

    def slider_pressed(self):
        print('被点击了')

    def slider_released(self):
        print('按钮释放')

app = QApplication(sys.argv)
window = myWindow()
window.show()

app.exec()