
def test__get__goketn__only_once(test_app):
    response = test_app.get('/api/v1/token')
    assert response.status_code == 200
    response = test_app.get('/api/v1/token')
    assert response.status_code == 401

def test__post_toketn__without_token_401(test_app):
    response = test_app.post('/api/v1/webhook')
    assert response.status_code == 401

