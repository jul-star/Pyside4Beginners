from PySide6.QtWidgets import QApplication
import sys
try:
    from button_holder import ButtonHolder 
except ImportError:
    from .button_holder import ButtonHolder

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()
app.exec()


"""
First version of example
app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Button example")

# button = QPushButton()
# button.setText("Press")
# window.setCentralWidget(button)


window.show()


app.exec()
"""