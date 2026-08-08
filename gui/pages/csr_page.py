from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout, QGroupBox, QHBoxLayout, QMessageBox, QComboBox,
    QFormLayout,
    QLineEdit
)

from gui.widgets.key_usage_widget import KeyUsageWidget
from gui.widgets.san_widget import SanWidget
from gui.dialogs.save_dialog import select_private_key_path, select_csr_path
from crypto.csr_builder import CSRBuilder
from crypto.export import export_pkey, export_csr
from models.csr_spec import CsrSpec
from models.key_specs import key_lengths, hash_algorithms

class CsrPage(QWidget):
    action_aborted = pyqtSignal()

    def __init__(self):
        super().__init__()

        title = QLabel("CSR Creator")
        title.setStyleSheet("font-size:24px; font-weight:bold;")

        layout = QVBoxLayout()

        # BEGIN SUBJECT
        subjectGroup = QGroupBox("Subject")

        subject_layout = QFormLayout()
        self.common_name = QLineEdit()
        self.organization = QLineEdit()
        self.organization_unit = QLineEdit()
        self.locality = QLineEdit()
        self.state= QLineEdit()
        self.country = QLineEdit()
        subject_layout.addRow("*Common Name:", self.common_name)
        subject_layout.addRow("*Organization:", self.organization)
        subject_layout.addRow("OU", self.organization_unit)
        subject_layout.addRow("Locality:", self.locality)
        subject_layout.addRow("State:", self.state)
        subject_layout.addRow("Country:", self.country)


        subjectGroup.setLayout(subject_layout)
        #END SUBJECT

        #BEGIN KEYGROUP
        key_group = QGroupBox("Key")
        key_layout = QFormLayout()
        self.key_algorithm = QComboBox()
        self.key_algorithm.addItems(["RSA", "ECDSA", "ED25519"])

        self.key_algorithm.currentTextChanged.connect(self.update_crypt_properties)

        self.key_specs = QComboBox()
        self.key_specs.addItems(key_lengths[self.key_algorithm.currentText()])

        self.hash_algorithm = QComboBox()
        self.hash_algorithm.addItems(hash_algorithms[self.key_algorithm.currentText()])

        key_layout.addRow("Key Algorithm:", self.key_algorithm)
        key_layout.addRow("Key Specs:", self.key_specs)
        key_layout.addRow("Hash Algorithm:", self.hash_algorithm)

        key_group.setLayout(key_layout)
        #END KEYGROUP

        #BEGIN SANWIDGET
        self.SANWidget = SanWidget()
        #END SANWIDGET

        #BEGIN KEYUSAGEWIDGET
        self.KeyUsageWidget = KeyUsageWidget()
        #END KEYUSAGEWIDGET

        # BEGIN BUTTONS
        Buttons = QHBoxLayout()

        b_abort = QPushButton("abort")
        b_abort.setFixedSize(200,50)
        b_abort.clicked.connect(
            self.abort_action
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
        layout.addWidget(key_group)
        layout.addWidget(self.SANWidget)
        layout.addWidget(self.KeyUsageWidget)
        layout.addLayout(Buttons)


        self.setLayout(layout)

    def abort_action(self):
        self.SANWidget.clear_table()
        self.action_aborted.emit()

    def continue_dialog(self):
        if not self.validate_input():
            return

        sans = self.SANWidget.get_entries()
        dns = []
        ip = []
        for san in sans:
            match san.type:
                case "IP": ip.append(san.value)
                case "DNS": dns.append(san.value)
                case _: QMessageBox().warning(self, " ", "san_widget Returned wrong type")

        csr_spec = CsrSpec(common_name=self.common_name.text(),
                                           organization=self.organization.text(),
                                           organizational_unit=self.organization_unit.text(),
                                           locality=self.locality.text(),
                                           state=self.state.text(),
                                           country=self.country.text().strip().upper(),
                                           key_algorithm=self.key_algorithm.currentText(),
                                           key_spec=self.key_specs.currentText(),
                                           signature_hash = self.hash_algorithm.currentText(),
                                           san_dns=dns,
                                           san_ip=ip,
                                           key_usage=self.KeyUsageWidget.export_key_usage(),
                                           extended_key_usage=self.KeyUsageWidget.export_key_extended_usage()
                                           )

        csr_builder = CSRBuilder(csr_spec)

        private_key = csr_builder.private_key

        csr = csr_builder.build()["certificate"]

        certpath = select_csr_path(parent=self)

        if not certpath:
            QMessageBox().warning(self, " ", "No csr file selected")
            return

        keypath = select_private_key_path()

        if not keypath:
            QMessageBox().warning(self, " ", "No private key file selected")
            return

        export_pkey(private_key, keypath)
        export_csr(csr, certpath)
        QMessageBox().information(self, "Export","Certificate successfully exported")
        return

    def validate_input(self) -> bool:
        if not self.common_name.text().strip() or not self.organization.text().strip():
            QMessageBox().warning(self, " ", "Please enter all * fields")
            return False

        if self.country.text() and len(self.country.text().strip()) != 2:
            QMessageBox().warning(self, " ", "Please enter a valid country code")
            return False

        return True

    def update_crypt_properties(self, algorithm: str):
        self.key_specs.clear()
        self.key_specs.addItems(key_lengths[algorithm])
        self.hash_algorithm.clear()
        self.hash_algorithm.addItems(hash_algorithms[algorithm])