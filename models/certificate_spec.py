from dataclasses import dataclass, field

@dataclass
class CertificateSpec:
    common_name: str = ""
    organization: str = ""
    organizational_unit: str = ""
    locality: str = ""
    state: str = ""
    country: str = ""
    key_algorithm: str = "RSA"
    key_size: int = 4096
    san_dns: list[str] = field(default_factory=list)
    san_ip: list[str] = field(default_factory=list)
    validity_days: int = 365
    is_ca: bool = False
    key_usage: list[str] = field(default_factory=list)
    extended_key_usage: list[str] = field(default_factory=list)
