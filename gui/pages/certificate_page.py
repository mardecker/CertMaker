from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout, QGroupBox, QHBoxLayout, QMessageBox, QComboBox,
    QFormLayout,
    QLineEdit
)

from gui.widgets.san_widget import SanWidget

keylengths = {
    "RSA": ["2048", "3072", "4096"],
    "ECDSA": ["P-256", "P-384", "P-521"],
    "ED25519": ["Ed25519"],
}

class CertificatePage(QWidget):
    action_aborted = pyqtSignal()

    def __init__(self):
        super().__init__()

        title = QLabel("CertMaker")
        title.setStyleSheet("font-size:24px; font-weight:bold;")

        layout = QVBoxLayout()

        # BEGIN SUBJECT
        subjectGroup = QGroupBox("Subject")

        subject_layout = QFormLayout()
        self.common_name = QLineEdit()
        self.organization = QLineEdit()
        self.organization_unit = QLineEdit()
        self.locality = QLineEdit()
        subject_layout.addRow("*Common Name:", self.common_name)
        subject_layout.addRow("*Organization:", self.organization)
        subject_layout.addRow("OU", self.organization_unit)
        subject_layout.addRow("Locality:", self.locality)

        subjectGroup.setLayout(subject_layout)
        #END SUBJECT

        #BEGIN KEYGROUP
        keyGroup = QGroupBox("Key")
        keyLayout = QFormLayout()
        self.key_algorithm = QComboBox()
        self.key_algorithm.addItems(["RSA", "ECDSA", "ED25519"])

        self.key_algorithm.currentTextChanged.connect(self.update_keylength)

        self.key_length = QComboBox()
        self.key_length.addItems(keylengths[self.key_algorithm.currentText()])

        keyLayout.addRow("Key Algorithm:", self.key_algorithm)
        keyLayout.addRow("Key Length:", self.key_length)

        keyGroup.setLayout(keyLayout)
        #END KEYGROUP

        #BEGIN SANWidget
        self.SANWidget = SanWidget()
        #END SANWidget

        # BEGIN BUTTONS
        Buttons = QHBoxLayout()

        b_abort = QPushButton("abort")
        b_abort.setFixedSize(200,50)
        b_abort.clicked.connect(
            self.action_aborted.emit
        )

        b_continue = QPushButton("continue")
        b_continue.setFixedSize(200, 50)
        b_continue.clicked.connect(
            self.continue_dialog
        )

        Buttons.addWidget(b_abort)
        Buttons.addWidget(b_continue)

        #END BUTTONS

        layout.addWidget(title)
        layout.setAlignment(title, Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop)
        Buttons.setAlignment(Qt.AlignmentFlag.AlignRight)


        layout.addWidget(subjectGroup)
        layout.addWidget(keyGroup)
        layout.addWidget(self.SANWidget)
        layout.addLayout(Buttons)


        self.setLayout(layout)

    def show_home_page(self):
        self.action_aborted.emit()

    def continue_dialog(self):
        if self.validate_input():
            print(self.common_name.text(), self.organization.text(), self.SANWidget.get_entries())

    def validate_input(self) -> bool:
        if not self.common_name.text().strip() or not self.organization.text().strip():
            QMessageBox().warning(self, " ", "Please enter all * fields")
            return False
        return True

    def update_keylength(self, algorithm: str):
        self.key_length.clear()
        self.key_length.addItems(keylengths[algorithm])