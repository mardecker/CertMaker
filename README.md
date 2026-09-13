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

_Self Signer_ is the main Form for creating Self Signed Certificates.
It's divided into the following sections:  

| Section | Description |
|---|---|
| [Subject](https://datatracker.ietf.org/doc/html/rfc5280#section-4.1.2.6) | General User **and** Issuer Informations | 
| Key | Hash / Key Algorithm and Key Spec Selection|
|[SAN](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.6)| List of Subject alternative Names (DNS-Names and IP-Addresses supported)|
|[Key Usage](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3)| Selectable use-cases supported by Certmaker |
|[Key Extended Usage](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.12)| Selectable extended use-cases supported by Certmaker|
|Additional Info| User defined Validity Days (how long your Certificate is valid), If its a CA and if the format should be PKCS12 (Unchecked equals PEM-Format)|

<img width="662" height="1164" alt="grafik" src="https://github.com/user-attachments/assets/0d4f2cac-800d-4b07-ab41-b6260d4e9169" />

When selecting "continue", you will be prompted to select the filepath(s) for your Certifikate-File (and depending if you chose the PEM Format your Key-File).
In addition, you may enter a passphrase to encrypt your privatekey.

### CSR Creator

It's a stipped down Version of _Self Signer_ for creating Certificate Signing Requests (CSRs).
The main difference is, that _CSR Creator_ doesn't let the user enter Additional Info (Validity Days, CA, Format) since this has to be handled by the Certification Authority issuing your certificate.

<img width="662" height="1061" alt="grafik" src="https://github.com/user-attachments/assets/8897312a-8088-4772-977a-8766687ed958" />




 
