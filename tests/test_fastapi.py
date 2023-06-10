
def test__get__goketn__only_once(test_app):
    response = test_app.get('/api/v1/token')
    assert response.status_code == 200
    response = test_app.get('/api/v1/token')
    assert response.status_code == 401