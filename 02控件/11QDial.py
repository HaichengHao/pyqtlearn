'''
最后，QDial 是一个可旋转的控件，功能与滑块相同，但外观为模拟拨盘。
它看起来很不错，但从 UI 角度来看并不特别用户友好。
然而，它们通常在音频应用程序中用作现实世界中的模拟拨盘的表示。
'''

import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDial, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')

        widget = QDial()
        widget.setRange(-10, 100)
        widget.setSingleStep(1)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print('值变换为', i)

    def slider_position(self, p):
        print('位置变化为:', p)

    def slider_pressed(self):
        print('按钮按下')

    def slider_released(self):
        print('按钮抬起')


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

'''
这些信号与 QSlider 的信号相同，并保留了相同的名称（例如 .sliderMoved）。

以上就是对 PyQt6 中可用的 Qt 控件的简要介绍'''