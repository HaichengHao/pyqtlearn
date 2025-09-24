'''
QSpinBox 提供了一个带箭头的小数字输入框，用于增加和减少值。
QSpinBox 支持整数，而相关的控件QDoubleSpinBox 支持浮点数。
'''

from PyQt6.QtWidgets  import QApplication, QSpinBox, QDoubleSpinBox,QMainWindow

import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        widget = QSpinBox()
        #或者
        # widget = QDoubleSpinBox()
        '''
        要设置可接受值的范围，您可以使用 setMinimum 和 setMaximum，
        或者使用 setRange 同时设置两者'''
        widget.setMinimum(-10)
        widget.setMaximum(3)
        #或者：widget.setRange(-10,3)
        '''
        值类型的标注支持在数字前添加前缀或在数字后添加后缀，
        例如使用 .setPrefix 和 .setSuffix 分别设置货币标记或单位'''
        widget.setPrefix('$')
        widget.setSuffix('c')
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print('数值变化为',i)

    def value_changed_str(self,s):
        print('字符变化为',s)

app = QApplication(
    sys.argv
)

window = MyWindow()
window.show()

app.exec()
'''
QSpinBox 和 QDoubleSpinBox 都具有 .valueChanged 信号，
该信号在其值发生改变时触发。.valueChanged 信号发送数字值（整数或浮点数），
而单独的 .textChanged 信号则将值作为字符串发送，包括前缀和后缀字符。'''