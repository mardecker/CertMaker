from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton, QLabel, QLineEdit, QGridLayout,
)

import gui.menubar as menubar
from gui import toolbar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setMinimumSize(400,400)

        self.menubar = menubar._create_menu(self)
        self.toolbar = toolbar._create_toolbar(self)

        #central = QWidget()
        #self.setCentralWidget(central)

        #layout = QVBoxLayout(central)

        #self.setLayout(layout)
