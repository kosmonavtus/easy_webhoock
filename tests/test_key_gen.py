import pytest

def test__generate_secret_key__is_bytes(generate_key):
    assert isinstance(generate_key, bytes)

def test__generate_secret_key__len_greater_or_eq(generate_key):
    assert len(generate_key) >= 64

def test__make_hmac_signature__is_str(generate_key, token, fabric_make_hmac_signature):
    hmac_signature = fabric_make_hmac_signature(generate_key, token)
    assert isinstance(hmac_signature, str)

def test__make_hmac_signature_is_type_error(token, fabric_make_hmac_signature):
    with pytest.raises(TypeError):
        fabric_make_hmac_signature(token, token)

@pytest.mark.parametrize(
    "received_token, expected_token, expected_result",
    [
        ("token", "token", True),
        ("token1", "token2", False),
        ("token", "TOKEN", False),
    ],
)

def test__verify_hmac__parametrize(fabric_verify_hmac, received_token, expected_token, expected_result):
    result = fabric_verify_hmac(received_token, expected_token)
    assert result == expected_result