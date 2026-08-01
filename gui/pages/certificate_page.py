from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout, QGroupBox, QHBoxLayout
)


class CertificatePage(QWidget):
    action_aborted = pyqtSignal()

    def __init__(self):
        super().__init__()

        title = QLabel("CertMaker")
        title.setStyleSheet("font-size:24px; font-weight:bold;")

        layout = QVBoxLayout()

        button = QPushButton("abort")
        button.setFixedSize(200,50)
        button.clicked.connect(
            self.action_aborted.emit
        )

        subjectGroup = QGroupBox("Subject")
        keyGroup = QGroupBox("Key")
        SANGoup = QGroupBox("SAN Goup")
        Buttons = QHBoxLayout()

        Buttons.addWidget(button)

        layout.addWidget(title)
        layout.setAlignment(title, Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(Buttons)


        self.setLayout(layout)

    def show_home_page(self):
        self.action_aborted.emit()