'''
您可以对任何 PyQt6 控件使用相同的模式。
如果控件未提供发送当前状态的信号，则您需要在处理程序中直接从控件检索该值。
例如，这里我们正在检查按下处理程序中的选中状态。
'''
import sys

from PyQt6.QtCore import Qt,QSize
from PyQt6.QtWidgets import QApplication,QPushButton,QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        self.button_is_checked = False #设置实例属性,让按钮先不被点选激活
        self.button = QPushButton('点我!!')
        self.button.setCheckable(True)
        self.button.released.connect(
            self.the_button_was_released
        ) #按钮一被释放(即不被激活状态,那就调用the_button_was_released函数)
        self.button.setChecked(self.button_is_checked)


        #设置窗口的中心控件
        self.setCentralWidget(self.button)

    def the_button_was_released(self):
        self.button_is_checked = self.button.isChecked() #tips:.isChecked() 返回按钮的检查状态。
        print(self.button_is_checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()