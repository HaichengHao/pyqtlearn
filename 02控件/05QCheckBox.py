'''
QCheckBox，顾名思义，它为用户提供了一个可选框。
然而，与所有 Qt 控件一样，它也有许多可配置的选项来更改控件的行为
'''
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QMainWindow
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        widget = QCheckBox('这是一个复选框')
        widget.setCheckState(Qt.CheckState.Checked)

        #对于三态:
        # widget.setCheckState(Qt.PartiallyChecked)
        # 或 widget.setTristate(True)
        widget.stateChanged.connect(self.show_state)  # 设置stateChanged的信号连接到槽show_state上面去

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(Qt.CheckState(s)) #检查是否被选中
        # print(Qt.CheckState.Checked)
        print(Qt.CheckState(s) == Qt.CheckState.Checked) #判断是否被点选
        print(s)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
'''
Qt.CheckState.Checked	该项已选中
Qt.CheckState.Unchecked	该项未选中
Qt.CheckState.PartiallyChecked	该项部分选中
'''



'''
可以使用 .setChecked 或 .setCheckState 通过编程方式设置复选框状态。
前者接受 True 或 False，分别代表已选中或未选中。
但是，使用 .setCheckState 时，
您还可以使用 Qt.命名空间标志指定部分选中状态。

支持部分选中状态（Qt.CheckState.PartiallyChecked）的复选框通常被称为“三态复选框”，即既非选中也非未选中。
处于此状态的复选框通常显示为灰色复选框，并常用于分层复选框布局中，其中子项与父级复选框相关联。

如果您将值设置为 Qt.CheckState.PartiallyChecked，复选框将变为三态——即具有三种可能的状态。您还可以通过使用 .setTristate(True)来达到相同的效果
'''