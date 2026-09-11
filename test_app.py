import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    """Test that / returns success"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['message'] == 'Hello from CI/CD!'

def test_health_endpoint(client):
    """Test that /api/health returns healthy"""
    response = client.get('/api/health')
    assert response.status_code == 200
    assert response.json['status'] == 'healthy'

def test_404_on_unknown_route(client):
    """Test that unknown routes return 404"""
    response = client.get('/nonexistent')
    assert response.status_code == 404