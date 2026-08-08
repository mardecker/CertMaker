import ipaddress

from cryptography import x509
from cryptography.hazmat._oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, ec, ed25519

from crypto.key_generator import generate_private_key
from models.csr_spec import CsrSpec

class CSRBuilder:
    def __init__(self, csr_spec: CsrSpec):
        self.csr_spec = csr_spec
        self.private_key = generate_private_key(csr_spec.key_algorithm, csr_spec.key_spec)
        self.public_key = self.private_key.public_key()

    def build(self  ):
        certificate = self.build_csr()
        return {
            "private_key": self.private_key,
            "certificate": certificate,
        }

    def build_csr(self):
        subject_attributes = []

        subject_attributes.append(
            x509.NameAttribute(
                NameOID.COMMON_NAME,
                self.csr_spec.common_name,
            )
        )

        subject_attributes.append(
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, self.csr_spec.organization)
        )

        if self.csr_spec.organizational_unit != "":
            subject_attributes.append(
                x509.NameAttribute(
                    NameOID.ORGANIZATIONAL_UNIT_NAME, self.csr_spec.organizational_unit
                )
            )

        if self.csr_spec.locality != "":
            subject_attributes.append(
                x509.NameAttribute(
                    NameOID.LOCALITY_NAME, self.csr_spec.locality
                )
            )

        if self.csr_spec.state != "":
            subject_attributes.append(
                x509.NameAttribute(
                    NameOID.STATE_OR_PROVINCE_NAME, self.csr_spec.state
                )
            )



        if self.csr_spec.country != "":
            subject_attributes.append(
                x509.NameAttribute(
                    NameOID.COUNTRY_NAME, self.csr_spec.country
                )
            )

        subject = x509.Name(subject_attributes)

        builder = (x509.CertificateSigningRequestBuilder()
                   .subject_name(subject)
                   )

        #add SAN entries
        san_entries = []
        for dns in self.csr_spec.san_dns:
            san_entries.append(
                x509.DNSName(dns)
            )

        for ip in self.csr_spec.san_ip:
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

        match self.csr_spec.signature_hash:
            case "SHA-256": sign_hash = hashes.SHA256()
            case "SHA-384": sign_hash = hashes.SHA384()
            case "SHA-512": sign_hash = hashes.SHA512()
            case "ED25519": sign_hash = None
            case _:
                raise ValueError(f"Unsupported signature algorithm: {self.csr_spec.signature_hash}")


        if isinstance(self.private_key,ed25519.Ed25519PrivateKey): #ed25519 can't hash stuff
            sign_hash = None

        # add Key Usage
        builder = builder.add_extension(
            self.csr_spec.key_usage,
            critical=True,
        )

        # add Key Extended Usage
        builder = builder.add_extension(
            x509.ExtendedKeyUsage(
                self.csr_spec.extended_key_usage
            ),
            critical=True,
        )

        return builder.sign(
            private_key=self.private_key,
            algorithm= sign_hash
        )