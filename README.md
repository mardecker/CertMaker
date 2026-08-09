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
```

## Instructions

When Executing the ```main.py```-File, you will be greeted by a select screen in which you may choose to create a new self-signed certificate or a new CSR.

<img width="662" height="660" alt="Select-Screen" src="https://github.com/user-attachments/assets/8948c6e1-8c02-4020-8e36-47cd99dbe169" />

According to your decision, you will be directed to either the _Self Signer_- or _CSR Creator_-From.

### Self Signer

#### Subject

#### Key

#### SAN

#### Key Usage

#### Key Extended Usage 

#### Additional Info



 
