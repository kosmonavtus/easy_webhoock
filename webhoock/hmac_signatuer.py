import hmac
import secrets


def make_hmac_signature(secret: bytes, token: str) -> str:
    hmac_signature = hmac.new(secret, token.encode(), "sha256").hexdigest()
    return hmac_signature


def generate_secret_key() -> bytes:
    secret_key = secrets.token_bytes(64)
    return secret_key


def verify_hmac(received_token: str, expected_token: str) -> bool:
    return hmac.compare_digest(received_token, expected_token)
