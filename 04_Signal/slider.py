#slider
from PySide6.QtWidgets import QApplication, QSlider
from PySide6.QtCore import Qt

def slider_value_changed(data):
    print("Slider value is ", data)


app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(0)
slider.setMaximum(10)
slider.setValue(5)

slider.valueChanged.connect(slider_value_changed)
slider.show()

app.exec()
