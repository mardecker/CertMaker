from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QGroupBox
from cryptography.x509.oid import ExtendedKeyUsageOID
from cryptography.x509 import KeyUsage

EXTENDED_KEY_USAGE = {
    "server_auth": {
        "name": "Server Authentication",
        "oid": ExtendedKeyUsageOID.SERVER_AUTH,
    },
    "client_auth": {
        "name": "Client Authentication",
        "oid": ExtendedKeyUsageOID.CLIENT_AUTH,
    },
    "code_signing": {
        "name": "Code Signing",
        "oid": ExtendedKeyUsageOID.CODE_SIGNING,
    },
}

class KeyUsageWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # BEGIN KEY-USAGE
        KeyUsageGroup = QGroupBox("Key Usage")
        KeyUsage_layout = QHBoxLayout()
        self.digital_signature = QCheckBox("Digital Signature")
        self.digital_signature.setChecked(True)
        self.key_enchipherment = QCheckBox("Key Encipherment")
        self.key_enchipherment.setChecked(True)
        self.key_agreement = QCheckBox("Key Agreement")
        self.key_certsign = QCheckBox("Key Certificate Signing")
        self.crl_sign = QCheckBox("CRL Signing")

        KeyUsage_layout.addWidget(self.digital_signature)
        KeyUsage_layout.addWidget(self.key_enchipherment)
        KeyUsage_layout.addWidget(self.key_agreement)
        KeyUsage_layout.addWidget(self.key_certsign)
        KeyUsage_layout.addWidget(self.crl_sign)
        KeyUsageGroup.setLayout(KeyUsage_layout)
        #END KEY-USAGE

        #BEGIN KEY-EXTENDED-USAGE
        KeyExtended_layout = QHBoxLayout()
        KeyExtended_layout.addWidget(QLabel("Key Extended Usage"))
        #END KEY-EXTENDED-USAGE

        layout.addWidget(KeyUsageGroup)
        layout.addLayout(KeyExtended_layout)
