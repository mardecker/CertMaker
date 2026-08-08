# CertMaker

**CertMaker** is a graphical user interface (GUI) for generating X.509 certificates and Certificate Signing Requests (CSRs).

The primary purpose of CertMaker is to simplify the creation of **self-signed certificates** and **CSRs** for common server- and client-side security scenarios, including:

- TLS
- Mutual TLS (mTLS)
- IKE / IPsec
- Other certificate-based authentication use cases

CertMaker is intended primarily for **development, testing, lab environments, and internal infrastructure**.

The generated certificates and CSRs are intended for the use cases supported by CertMaker. The application does not aim to provide certificate profiles for every possible X.509 use case, such as S/MIME or other specialized certificate applications.

## Dependencies

CertMaker is built using:

- [PyQt6](https://pypi.org/project/PyQt6/) – graphical user interface
- [cryptography](https://pypi.org/project/cryptography/) – certificate and cryptographic operations

The required dependencies can be installed manually or automatically by installing the project:

```bash
pip install .
