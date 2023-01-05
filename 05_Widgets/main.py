# main

from PySide6.QtWidgets import QApplication, QMainWindow
from main_window import MainWindow
import sys


app = QApplication(sys.argv)
window = MainWindow(app)
window.show()

app.exec()




"""
Version of RockWidget

from rock_widget import RockWidget
app = QApplication(sys.argv)
window =QMainWindow()
rw = RockWidget()
window.setCentralWidget(rw)
window.show()
app.exec()
"""