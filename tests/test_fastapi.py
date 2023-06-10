

def test__get__goketn(test_app):
    response = test_app.get('/api/v1/token')
    assert response.status_code == 200