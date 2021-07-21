import pytest

from app import api

@pytest.fixture()
def app():
    app = api
    return app

def test_float(client):
    response = client.post('/math', json={"num": "3.1"})
    assert response.status_code == 400

def test_alpha(client):
    response = client.post('/math', json={"num": "abc"})
    assert response.status_code == 400

def test_limit(client):
    response = client.post('/math', json={"num": "9000"})
    assert response.status_code == 400

def test_json(client):
    response = client.post("/math", json={})
    assert response.status_code == 400