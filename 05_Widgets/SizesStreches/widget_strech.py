from PySide6.QtWidgets import QWidget, QTableWidget, QLabel
from PySide6.QtWidgets import QSizePolicy, QHBoxLayout
from PySide6.QtCore import QSize

class WidgetStretch(QWidget):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.layout = QHBoxLayout(self)
        self.init_label()
        self.init_table()

    def init_label(self):
        label = QLabel("Label 1")
        label.setMinimumSize(QSize(64,32))
        label.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.layout.addWidget(label,1)

    def init_table(self):
        table = QTableWidget(self)
        table.setMinimumSize(QSize(300, 300))
        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        table.setRowCount(5)
        # table.insertRow(5)
        table.setColumnCount(3)
        # table.insertColumn(3)        
        table.setWindowTitle("My table")        
        self.layout.addWidget(table,2)