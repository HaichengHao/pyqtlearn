import sys
from PyQt6.QtWidgets import QApplication,QPushButton
import sys

app = QApplication(sys.argv)

window = QPushButton('点我')

window.show()

app.exec()

