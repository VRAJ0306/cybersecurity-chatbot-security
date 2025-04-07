import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_chat_endpoint_without_api_key(client):
    response = client.post('/chat', json={'message': 'Hello'})
    assert response.status_code == 401

def test_chat_endpoint_with_api_key(client):
    headers = {'x-api-key': 'your-secure-api-key'}
    response = client.post('/chat', json={'message': '<script>alert("x")</script> Hello!'}, headers=headers)
    assert response.status_code == 200
    data = response.get_json()
    assert "Processed:" in data['response']
