import pytest
from hmac_signatuer import generate_secret_key, make_hmac_signature, verify_hmac


@pytest.fixture
def generate_key():
    key = generate_secret_key()
    return key

@pytest.fixture
def token():
    return 'example_token_for_test'

@pytest.fixture
def fabric_make_hmac_signature():
    return make_hmac_signature

@pytest.fixture
def fabric_verify_hmac():
    return verify_hmac