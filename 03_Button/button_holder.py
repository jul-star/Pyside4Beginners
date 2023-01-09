# button_holder
from PySide6.QtWidgets import QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Button Holder App")
        button = QPushButton("Press me")

        #Set up the button :
        self.setCentralWidget(button)



