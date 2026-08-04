from PyQt6.QtWidgets import QFileDialog


def select_private_key_path(parent=None):
    filename, _ = QFileDialog.getSaveFileName(
        parent,
        "Privaten Schlüssel speichern",
        "key.pem",
        "Private Key (*.key *.pem)"
    )

    return filename


def select_certificate_path(parent=None, is_p12=False):
    directory = "crt.pem"
    filter= "Certificate (*.crt *.cer *.pem)"
    if is_p12:
        directory = "crt.p12"
        filter = "Certificate (*.pfx *.p12)"

    filename, _ = QFileDialog.getSaveFileName(
        parent,
        "Zertifikat speichern",
        directory,
        filter
    )

    return filename