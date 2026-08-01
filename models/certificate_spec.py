CertificateSpec(
    common_name="server01.local",
    organization="Example GmbH",
    country="DE",

    key_algorithm="RSA",
    key_size=4096,

    san_dns=[
        "server01.local",
        "www.server01.local"
    ],

    san_ip=[
        "192.168.1.10"
    ],

    validity_days=365,

    is_ca=False,

    key_usage=[
        "Digital Signature",
        "Key Encipherment"
    ],

    eku=[
        "Server Authentication"
    ]
)