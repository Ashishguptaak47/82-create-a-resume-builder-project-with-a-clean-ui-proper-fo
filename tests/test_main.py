import pytest
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Resume Builder' in response.data

def test_generate(client):
    response = client.post('/generate', data={
        'name': 'Test User',
        'email': 'test@example.com',
        'phone': '1234567890',
        'website': 'example.com',
        'summary': 'A test summary',
        'experience': 'A test experience',
        'education': 'A test education',
        'skills': 'Python'
    })
    assert response.status_code == 200
