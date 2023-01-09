from PySide6.QtWidgets import QApplication, QPushButton
import sys


def button_clicked():
    print("Button was clicked")

app = QApplication()

button = QPushButton()
button.setText("Press")
button.clicked.connect(button_clicked)

button.show()

app.exec()