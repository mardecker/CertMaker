from unittest import case

from cryptography.hazmat.primitives.asymmetric import rsa, ec, ed25519
from models.certificate_spec import CertificateSpec


class CertificateBuilder:
    def __init__(self, certificate_spec: CertificateSpec):
        self.certificate_spec = certificate_spec

        match self.certificate_spec.key_algorithm:
            case "RSA":
                self.gen_rsa_key()
            case "ECDSA":
                self.gen_ecdsa_key()
            case "ED25519":
                self.gen_ed25519_key()
            case _:
                raise ValueError(
                    f"Unsupported key algorithm: {self.certificate_spec.key_algorithm}"
                )

    def gen_rsa_key(self):
        key_size = int(self.certificate_spec.key_spec)
        return rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size,
        )

    def gen_ecdsa_key(self):
        key_spec = self.certificate_spec.key_spec
        match key_spec:
            case "P-256":
                secp_alg = ec.SECP256R1()
            case "P-384":
                secp_alg = ec.SECP384R1()
            case "P-512":
                secp_alg = ec.SECP256R1()
            case _:
                raise ValueError("Unsupported ECDSA algorithm")
        return ec.generate_private_key(
            secp_alg
        )

    def gen_ed25519_key(self):
        return ed25519.Ed25519PrivateKey.generate()