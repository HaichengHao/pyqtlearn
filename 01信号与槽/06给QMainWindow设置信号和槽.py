from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from PyQt6.QtCore import Qt, QSize

from random import choice

window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]  # 1


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n_times_clicked = 0
        self.button = QPushButton('点击我')
        self.button.clicked.connect(self.the_btn_was_clicked)

        #tips:将我们的自定义槽方法 the_window_title_changed 连接到 windows的.windowTitleChanged 信号。

        self.windowTitleChanged.connect(
            self.the_window_title_changed
        )
        # 设置窗口的中心控件
        self.setCentralWidget(self.button)

    def the_btn_was_clicked(self):
        print('按钮被点击了')
        new_window_title = choice(window_titles)
        print(f'新的标题是:{new_window_title}')
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print(f'窗口标题更换{window_title}')

        if window_title == "Something went wrong":
            self.button.setDisabled(True)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

'''一些疑问
the_window_title_changed中window_title参数从哪里来
答:信号中携带的
windowTitleChanged 这个信号不是空的，它携带了数据。具体来说，它携带了新的窗口标题作为参数。

你可以查看 Qt 的官方文档，windowTitleChanged 信号的定义通常是这样的：

cpp
void windowTitleChanged(const QString &title)
这表示它会发出一个信号，并将新的标题（title）作为一个字符串参数传递出去。


定义的 the_window_title_changed 方法就是一个槽函数（slot）。当你用 connect() 方法将信号连接到这个槽函数时，你实际上是在说：
“每当 windowTitleChanged 信号被发出时，请调用 the_window_title_changed 这个方法，并把信号携带的参数（新的标题）传给它。”
因此，window_title 这个参数是由 Qt 框架在信号发出时自动传递进来的，你不需要手动去调用或赋值。

如何知道信号会传递什么参数？
查看官方文档：最权威的方式是查阅 Qt 的 C++ 文档（PyQt 的文档通常链接到 Qt 文档）。搜索 QWidget 或 QMainWindow 的 windowTitleChanged 信号，你会看到它声明了参数。
IDE 的智能提示：好的 IDE（如 PyCharm）在你输入 self.windowTitleChanged. 时，通常会提示 connect 方法，并显示信号的签名（参数类型）。
经验：常见的信号如 clicked() 通常不带参数，textChanged(str) 带一个字符串，valueChanged(int) 带一个整数等。
总结
window_title 参数是 windowTitleChanged 信号在被发出时自动传递的。你不需要关心它是如何“进来”的，你只需要知道：每当窗口标题改变，这个方法就会被调用，并且 window_title 就是改变后的新标题。这就是信号与槽机制的强大之处——它实现了对象间的松耦合通信。
'''