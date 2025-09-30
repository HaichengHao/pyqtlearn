
'''
为了更方便地可视化布局，我们将首先创建一个简单的自定义控件来显示我们选择的纯色。
这有助于区分我们添加到布局中的控件。请您在与脚本相同的文件夹中创建一个新文件，
并将其命名为 layout_colorwidget.py，并添加以下代码。我们将在下一个示例中将此代码导入到我们的应用程序中。
'''
from PyQt6.QtGui import QColor,QPalette #palette调色板
from PyQt6.QtWidgets import QWidget

class Color(QWidget):
    def __init__(self,color):
        super().__init__()
        self.setAutoFillBackground(True) #设置自动填充背景为True

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window,QColor(color))
        self.setPalette(palette)
'''
在此代码中，我们子类化 QWidget 以创建自己的自定义控件 Color。
创建控件时，我们接受一个参数——颜色（一个字符串）。
首先，我们将 .setAutoFillBackground 设置为 True，
以指示控件自动用窗口颜色填充其背景。
接下来，我们将控件的 QPalette.Window 颜色更改为我们提供的值 color 所描述的新 QColor。
最后，我们将该调色板应用回控件。最终结果是一个填充了纯色的控件，该颜色是在创建控件时指定的

如果您觉得以上内容有些难以理解，请不要担心！我们将在后面详细介绍如何创建自定义控件和调色板。目前，您只需了解以下代码即可创建一个实心填充的红色控件即可——
Color('red')
'''