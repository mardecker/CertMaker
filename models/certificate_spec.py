from dataclasses import dataclass, field
from cryptography.x509.oid import ExtendedKeyUsageOID
from cryptography.x509 import KeyUsage

DEFAULT_KEY_USAGE = KeyUsage(
    digital_signature=False,
    content_commitment=False,
    key_encipherment=False,
    data_encipherment=False,
    key_agreement=False,
    key_cert_sign=False,
    crl_sign=False,
    encipher_only=False,
    decipher_only=False,
)

@dataclass
class CertificateSpec:
    common_name: str = ""
    organization: str = ""
    organizational_unit: str = ""
    locality: str = ""
    state: str = ""
    country: str = ""
    key_algorithm: str = "RSA"
    key_spec: str = "4096"
    signature_hash: str = "SHA256"
    san_dns: list[str] = field(default_factory=list)
    san_ip: list[str] = field(default_factory=list)
    validity_days: int = 365
    is_ca: bool = False
    key_usage: KeyUsage = DEFAULT_KEY_USAGE
    extended_key_usage: list[ExtendedKeyUsageOID] = field(default_factory=list)
