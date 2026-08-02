from PyQt6.QtWidgets import QFileDialog


def select_private_key_path(parent=None):
    filename, _ = QFileDialog.getSaveFileName(
        parent,
        "Privaten Schlüssel speichern",
        "key.pem",
        "Private Key (*.key *.pem)"
    )

    return filename


def select_certificate_path(parent=None):
    filename, _ = QFileDialog.getSaveFileName(
        parent,
        "Zertifikat speichern",
        "crt.pem",
        "Certificate (*.crt *.cer *.pem)"
    )

    return filename