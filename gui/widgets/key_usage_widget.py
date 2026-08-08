from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QGroupBox, QGridLayout
from cryptography.x509.oid import ExtendedKeyUsageOID
from cryptography.x509 import KeyUsage

class KeyUsageWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        # BEGIN KEY-USAGE
        KeyUsageGroup = QGroupBox("Key Usage")
        KeyUsage_layout = QGridLayout()
        self.digital_signature = QCheckBox("Digital Signature")
        self.digital_signature.setChecked(True)
        self.key_encipherment = QCheckBox("Key Encipherment")
        self.key_agreement = QCheckBox("Key Agreement")
        self.key_cert_sign = QCheckBox("Key Certificate Signing")
        self.crl_sign = QCheckBox("CRL Signing")

        KeyUsage_layout.addWidget(self.digital_signature,0,0)
        KeyUsage_layout.addWidget(self.key_encipherment,0,1)
        KeyUsage_layout.addWidget(self.key_cert_sign,0,2)
        KeyUsage_layout.addWidget(self.crl_sign,1,0)
        KeyUsageGroup.setLayout(KeyUsage_layout)
        #END KEY-USAGE

        #BEGIN KEY-EXTENDED-USAGE
        KeyExtendedGroup = QGroupBox("Key Extended Usage")
        KeyExtended_layout = QGridLayout()

        self.server_auth = QCheckBox("Server Authentication")
        self.server_auth.setChecked(True)
        self.client_auth = QCheckBox("Client Authentication")
        self.client_auth.setChecked(True)
        self.code_signing = QCheckBox("Code Signing")
        self.ipsec_ike = QCheckBox("IPSEC IKE")

        KeyExtended_layout.addWidget(self.server_auth,0,0)
        KeyExtended_layout.addWidget(self.client_auth,0,1)
        KeyExtended_layout.addWidget(self.code_signing,0,2)
        KeyExtended_layout.addWidget(self.ipsec_ike,1,0)

        KeyExtendedGroup.setLayout(KeyExtended_layout)
        #END KEY-EXTENDED-USAGE

        layout.addWidget(KeyUsageGroup)
        layout.addWidget(KeyExtendedGroup)

    def export_key_usage(self) -> KeyUsage:
        return KeyUsage(
            digital_signature=self.digital_signature.isChecked(),
            content_commitment=False,
            key_encipherment=self.key_encipherment.isChecked(),
            data_encipherment=False,
            key_agreement=False,
            key_cert_sign=self.key_cert_sign.isChecked(),
            crl_sign=self.crl_sign.isChecked(),
            encipher_only=False,
            decipher_only=False,
        )

    def export_key_extended_usage(self) -> list[ExtendedKeyUsageOID]:
        extended_usage = []
        if self.server_auth.isChecked():
            extended_usage.append(ExtendedKeyUsageOID.SERVER_AUTH)
        if self.client_auth.isChecked():
            extended_usage.append(ExtendedKeyUsageOID.CLIENT_AUTH)
        if self.code_signing.isChecked():
            extended_usage.append(ExtendedKeyUsageOID.CODE_SIGNING)
        if self.ipsec_ike.isChecked():
            extended_usage.append(ExtendedKeyUsageOID.IPSEC_IKE)
        return extended_usage
