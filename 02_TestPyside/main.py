from PySide6.QtWidgets import QApplication, QWidget, QPushButton

# command line arguments
import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()
# Start the event loop
button = QPushButton()
button.setText("Hello")


app.exec()