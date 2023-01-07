from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtCore import QSize
from PySide6.QtWidgets import QSizePolicy

class WidgetSize(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.layout = QHBoxLayout(self)
        self.init_label()
        self.init_button()
        self.init_editline()

    def init_editline(self):
        line = QLineEdit()
        line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        line.setMinimumSize(QSize(100,32))
        self.layout.addWidget(line)

    def init_button(self):
        button = QPushButton("Press")
        button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        button.setMinimumSize(QSize(64, 32))
        self.layout.addWidget(button)

    def init_label(self):        
        label = QLabel("Label1")
        label.setMinimumSize(QSize(64, 32))
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layout.addWidget(label)
        

        