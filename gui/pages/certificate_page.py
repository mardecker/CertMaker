from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout, QGroupBox, QHBoxLayout, QMessageBox,
    QFormLayout,
    QLineEdit
)


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

        keyGroup = QGroupBox("Key")
        SANGoup = QGroupBox("SAN Goup")


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
        layout.addLayout(Buttons)


        self.setLayout(layout)

    def show_home_page(self):
        self.action_aborted.emit()

    def continue_dialog(self):
        if self.validate_input():
            print(self.common_name.text(), self.organization.text())

    def validate_input(self) -> bool:
        if not self.common_name.text().strip() or not self.organization.text().strip():
            QMessageBox().warning(self, " ", "Please enter all * fields")
            return False
        return True