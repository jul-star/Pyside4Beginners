from PySide6.QtWidgets import QApplication
import sys
from widget_strech import WidgetStretch

if __name__ == "__main__":
    app = QApplication()
    window = WidgetStretch(app)
    window.show()

    app.exec()

"""
Version WidgetSize
from widget_size import WidgetSize


if __name__ == "__main__":
    app = QApplication()
    window = WidgetSize(app)
    window.show()

    app.exec()
"""