from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton, QLabel, QLineEdit, QGridLayout,
)

import gui.menubar as menubar
from gui import toolbar
from gui.dialogs.certificate_dialog import run_certificate_dialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.setMinimumSize(800,600)

        self.menubar = menubar._create_menubar(self)
        #self.toolbar = toolbar._create_toolbar(self)

        self.button = QPushButton("Create new Certificate")
        self.button.setFixedSize(200, 50)
        self.button.clicked.connect(self.create_certificate)

        container = QWidget()
        layout = QGridLayout(container)
        layout.addWidget(self.button, 2, 2)

        self.setCentralWidget(container)

    def create_certificate(self):
        run_certificate_dialog()
