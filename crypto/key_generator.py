from cryptography.hazmat.primitives.asymmetric import rsa, ec, ed25519

def generate_private_key(type: str, spec: str):
    match type:
        case "RSA":
            key = gen_rsa_key(spec)
        case "ECDSA":
            key = gen_ecdsa_key(spec)
        case "ED25519":
            key = gen_ed25519_key(spec)
        case _:
            raise ValueError(
                f"Unsupported key algorithm: {type}"
            )
    return key


def gen_rsa_key(spec: str):
    key_size = int(spec)
    return rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
    )


def gen_ecdsa_key(spec: str):
    match spec:
        case "P-256":
            spec_alg = ec.SECP256R1()
        case "P-384":
            spec_alg = ec.SECP384R1()
        case "P-521":
            spec_alg = ec.SECP521R1()
        case _:
            raise ValueError("Unsupported ECDSA algorithm")
    return ec.generate_private_key(
        spec_alg
    )


def gen_ed25519_key(self):
    return ed25519.Ed25519PrivateKey.generate()