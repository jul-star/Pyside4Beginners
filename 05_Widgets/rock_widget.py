from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout
from PySide6.QtCore import Qt
import sys

class RockWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("RockWidget")

        b1 = QPushButton("Button 1")
        b1.clicked.connect(self.b1_clicked)

        b2 = QPushButton("Button 2")
        b2.clicked.connect(self.b2_clicked)

        layout = QHBoxLayout()
        layout.addWidget(b1)
        layout.addWidget(b2)
        self.setLayout(layout)
    
    def b1_clicked(self):
        print("B1 is clicked")
    
    def b2_clicked(self):
        print("B2 is clicked")


