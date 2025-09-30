import sys
from layout_colorwidget import Color
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLabel, QMainWindow,
                             QStackedLayout, QHBoxLayout, QVBoxLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('vimin')
        self.setWindowIcon(QIcon('../appicon.png'))

        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()  # 按钮横着排序
        self.stacked_layout = QStackedLayout()

        # 纵向排布,上面是按钮,下面是堆叠标签页
        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stacked_layout)

        btn = QPushButton('red')
        btn.pressed.connect(self.active_tab_1)
        button_layout.addWidget(btn)
        self.stacked_layout.addWidget(Color('red'))

        btn = QPushButton('green')
        btn.pressed.connect(self.active_tab_2)
        button_layout.addWidget(btn)
        self.stacked_layout.addWidget(Color('green'))

        btn = QPushButton('yellow')
        btn.pressed.connect(self.active_tab_3)
        button_layout.addWidget(btn)
        self.stacked_layout.addWidget(Color('yellow'))

        #创建容器组件来进行布局的添加
        container = QWidget()
        container.setLayout(page_layout)
        self.setCentralWidget(container)

    def active_tab_1(self):
        self.stacked_layout.setCurrentIndex(0)

    def active_tab_2(self):
        self.stacked_layout.setCurrentIndex(1)

    def active_tab_3(self):
        self.stacked_layout.setCurrentIndex(2)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
