def test_home_page(client):
    """Проверяем, что главная страница возвращает 200 OK"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello' in response.data

def test_api_status(client):
    """Проверяем API эндпоинт"""
    response = client.get('/api/status')
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert data['status'] == 'ok'