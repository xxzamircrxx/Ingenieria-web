import pytest
from src.app import app

@pytest.fixture
def client():
    return app.test_client()

def test_post_item(client):
    res = client.post('/items', json={"name": "test"})
    assert res.status_code == 201

def test_get_items(client):
    res = client.get('/items')
    assert res.status_code == 200

def test_delete_item(client):
    client.post('/items', json={"name": "test"})
    res = client.delete('/items/0')
    assert res.status_code == 204

def test_delete_not_found(client):
    res = client.delete('/items/999')
    assert res.status_code == 404

def test_multiple_posts(client):
    client.post('/items', json={"a":1})
    client.post('/items', json={"b":2})
    res = client.get('/items')
    assert res.status_code == 200