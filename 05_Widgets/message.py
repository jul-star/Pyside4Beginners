from PySide6.QtWidgets import QMessageBox


class Message():
    def __init__(self, parent) -> None:
        self.parent = parent
        self.ret = ""

    def critical(self):        
        msg = QMessageBox()
        msg.setMinimumSize(700,200)
        msg.setWindowTitle("Critical message:")
        msg.setText("Hello, Jul")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.setDefaultButton(QMessageBox.Ok)
        self.ret = msg.exec()
        self.getMsgReturn()
    
    def getMsgReturn(self):
        if (self.ret == QMessageBox.Ok):
            self.parent.GetMsg("Ok")
            return
        if (self.ret == QMessageBox.Cancel):
            self.parent.GetMsg("Cancel")
            return
        self.parent.GetMsg("Nothing")

