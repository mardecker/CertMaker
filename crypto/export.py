from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import pkcs12, BestAvailableEncryption

# save private key:
def export_pkey(private_key, path):
    with open (path, "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )
# save certificate
def export_certificate(certificate, path):
    with open (path, "wb") as f:
        f.write(
            certificate.public_bytes(
                encoding=serialization.Encoding.PEM,
            )
        )


def export_pkcs12(certificate, private_key, path, friendly_name):
    p12_data = pkcs12.serialize_key_and_certificates(
        name=friendly_name.encode(),
        key=private_key,
        cert=certificate,
        cas=None,
        encryption_algorithm=serialization.NoEncryption(),
    )

    with open(path, "wb") as f:
        f.write(p12_data)