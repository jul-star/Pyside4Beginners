from message import Message
from PySide6.QtWidgets import QMainWindow
from PySide6.QtWidgets import QPushButton
from PySide6.QtCore import QSize

class MyApp(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.msg = Message(self)

        b1 = QPushButton("Critical")        
        b1.setFixedSize(QSize(64,64))
        b1.clicked.connect(self.msg.critical)
        b1.clicked.connect()

        self.layout().addChildWidget(b1)
        self.ret = ""

    def GetMsg(self, val):
        print("GetMsg: ", val)

    def b1_clicked(self):
        print("B1 is clicked")