import pytest
from app import app as flask_app  # ← Импортируем как 'flask_app'

@pytest.fixture
def app():
    """Создаёт и настраивает тестовое приложение"""
    flask_app.config['TESTING'] = True  # ← Используем 'flask_app'
    flask_app.config['WTF_CSRF_ENABLED'] = False
    yield flask_app  # ← Возвращаем 'flask_app'

@pytest.fixture
def client(app):
    """Создаёт тестовый клиент"""
    return app.test_client()