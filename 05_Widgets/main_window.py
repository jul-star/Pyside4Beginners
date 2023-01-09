# menu
from PySide6.QtWidgets import QMenuBar, QMenu, QToolBar, QMainWindow
from PySide6.QtWidgets import QStatusBar
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon


class MainWindow(QMainWindow):
    def __init__(self, app) -> None:
        super().__init__()
        self.app = app #declare an app member
        self.setWindowTitle("My Window")

        #Menubar and menus

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")        
        quit_action = file_menu.addAction("Quit")

        edit_menu = menu_bar.addMenu("&Edit")
        edit_action = edit_menu.addAction("Edit")
        cut_action = edit_menu.addAction("Cut")
        undo_action = edit_menu.addAction("Undo")
        redo_action = edit_menu.addAction("Redo")

        window_menu = menu_bar.addMenu("&Window")
        settings_menu = menu_bar.addMenu("&Settings")

        quit_action.triggered.connect(self.quit_app)

        toolbar = QToolBar("My toolbar")
        toolbar.setIconSize(QSize(10,10))        

        quit_toolbar = toolbar.addAction("Quit")
        quit_toolbar.triggered.connect(self.quit_app)


        a1 = QAction("Some action", self)
        a1.setStatusTip("Status message")
        a1.triggered.connect(self.tool_bar_a1)
        toolbar.addAction(a1)

        a2 = QAction("Other Action", self)
        a2.setStatusTip("A2 status")
        a2.triggered.connect(self.tool_bar_a2)
        toolbar.addAction(a2)

        a3 = QAction(QIcon("01.png"), "A3",self)
        a3.setStatusTip("A3 status")
        a3.triggered.connect(self.tool_bar_a3)
        toolbar.addAction(a3)

        self.addToolBar(toolbar)

        self.setStatusBar(QStatusBar(self))
        

    def tool_bar_a1(self):
        print("tool_bar_action 1")
    
    def tool_bar_a2(self):
        print("tool_bar_action 2")

    def tool_bar_a3(self):
        self.statusBar().showMessage("Hello from A3",3000) # milliseconde

    def quit_app(self):
        print("Quit app")
        self.app.quit()
        print("Quit app quit")

