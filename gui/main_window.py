from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle("CertMaker")
        self.setMinimumSize(400,400)

        button = QPushButton("Push me")
        button.setFixedSize(100,40)
        button.clicked.connect(self.the_button_clicked)

        self.setCentralWidget(button)

    def the_button_clicked(self):
        print("clicked")

