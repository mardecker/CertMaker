from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class HomePage(QWidget):

    create_certificate_requested = pyqtSignal()
    create_csr_requested = pyqtSignal()

    def __init__(self):
        super().__init__()

        title = QLabel("CertManager")
        title.setStyleSheet("font-size:24px; font-weight:bold;")

        certificate_button = QPushButton("Create new Certificate")
        csr_button = QPushButton("Create new CSR")

        certificate_button.setFixedSize(250, 50)
        csr_button.setFixedSize(250, 50)

        certificate_button.clicked.connect(
            self.create_certificate_requested.emit
        )

        csr_button.clicked.connect(
            self.create_csr_requested.emit
        )

        layout = QVBoxLayout()

        layout.addStretch()
        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(certificate_button)
        layout.addWidget(csr_button)
        layout.addStretch()

        layout.setAlignment(title, Qt.AlignmentFlag.AlignCenter)
        layout.setAlignment(certificate_button, Qt.AlignmentFlag.AlignHCenter)
        layout.setAlignment(csr_button, Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(layout)