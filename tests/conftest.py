import pytest
from webhoock.hmac_signatuer import generate_secret_key, make_hmac_signature, verify_hmac
from fastapi.testclient import TestClient
from webhoock.app import easy_webhoock

app = easy_webhoock()

@pytest.fixture
def test_app():
    with TestClient(app, headers={"localhost": "127.0.0.1"}) as client:
        yield client


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