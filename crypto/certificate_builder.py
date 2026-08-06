import datetime
import ipaddress

from cryptography import x509
from cryptography.hazmat._oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, ec, ed25519

from models.certificate_spec import CertificateSpec


class CertificateBuilder:
    def __init__(self, cert_spec: CertificateSpec):
        self.certificate_spec = cert_spec
        self.private_key = self.generate_private_key()
        self.public_key = self.private_key.public_key()

    def build(self  ):
        certificate = self.build_certificate()
        return {
            "private_key": self.private_key,
            "certificate": certificate,
        }

    def build_certificate(self):
        subject_attributes = []

        subject_attributes.append(
            x509.NameAttribute(
                NameOID.COMMON_NAME,
                self.certificate_spec.common_name,
            )
        )

        subject_attributes.append(
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, self.certificate_spec.organization)
        )

        if self.certificate_spec.organizational_unit != "":
            subject_attributes.append(
                x509.NameAttribute(
                    NameOID.ORGANIZATIONAL_UNIT_NAME, self.certificate_spec.organizational_unit
                )
            )

        if self.certificate_spec.locality != "":
            subject_attributes.append(
                x509.NameAttribute(
                    NameOID.LOCALITY_NAME, self.certificate_spec.locality
                )
            )

        if self.certificate_spec.state != "":
            subject_attributes.append(
                x509.NameAttribute(
                    NameOID.STATE_OR_PROVINCE_NAME, self.certificate_spec.state
                )
            )



        if self.certificate_spec.country != "":
            subject_attributes.append(
                x509.NameAttribute(
                    NameOID.COUNTRY_NAME, self.certificate_spec.country
                )
            )

        subject = issuer = x509.Name(subject_attributes)

        builder = (x509.CertificateBuilder()
                   .subject_name(subject)
                   .issuer_name(issuer)
                   .public_key(self.public_key)
                   .serial_number(x509.random_serial_number())
                   .not_valid_before(datetime.datetime.now(datetime.timezone.utc))
                   .not_valid_after(datetime.datetime.now(datetime.timezone.utc)
                                    + datetime.timedelta(days=self.certificate_spec.validity_days))
                   )

        builder = builder.add_extension(
            x509.BasicConstraints(
                ca=self.certificate_spec.is_ca,
                path_length=None
            ),
            critical=True,
        )

        #add SAN entries
        san_entries = []
        for dns in self.certificate_spec.san_dns:
            san_entries.append(
                x509.DNSName(dns)
            )

        for ip in self.certificate_spec.san_ip:
            san_entries.append(
                x509.IPAddress(
                    ipaddress.ip_address(ip))
            )

        if san_entries:
            builder = builder.add_extension(
                x509.SubjectAlternativeName(san_entries),
                critical=False,
            )

        sign_hash = hashes.SHA256() # default case

        match self.certificate_spec.signature_hash:
            case "SHA-256": sign_hash = hashes.SHA256()
            case "SHA-384": sign_hash = hashes.SHA384()
            case "SHA-512": sign_hash = hashes.SHA512()
            case "ED25519": sign_hash = None
            case _:
                raise ValueError(f"Unsupported signature algorithm: {self.certificate_spec.signature_hash}")


        if isinstance(self.private_key,ed25519.Ed25519PrivateKey): #ed25519 can't hash stuff
            sign_hash = None

        # add Key Usage
        builder = builder.add_extension(
            self.certificate_spec.key_usage,
            critical=True,
        )

        # add Key Extended Usage
        builder = builder.add_extension(
            x509.ExtendedKeyUsage(
                self.certificate_spec.extended_key_usage
            ),
            critical=True,
        )

        return builder.sign(
            private_key=self.private_key,
            algorithm= sign_hash
        )

    def generate_private_key(self):
        match self.certificate_spec.key_algorithm:
            case "RSA":
                key = self.gen_rsa_key()
            case "ECDSA":
                key = self.gen_ecdsa_key()
            case "ED25519":
                key = self.gen_ed25519_key()
            case _:
                raise ValueError(
                    f"Unsupported key algorithm: {self.certificate_spec.key_algorithm}"
                )
        return key


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
            case "P-521":
                secp_alg = ec.SECP521R1()
            case _:
                raise ValueError("Unsupported ECDSA algorithm")
        return ec.generate_private_key(
            secp_alg
        )

    def gen_ed25519_key(self):
        return ed25519.Ed25519PrivateKey.generate()