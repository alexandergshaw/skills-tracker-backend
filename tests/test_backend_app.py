import pytest
from backend_app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_welcome(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data

def test_skills(client):
    response = client.get('/api/skills')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_projects(client):
    response = client.get('/api/projects')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_skill_usage(client):
    response = client.get('/api/skill-usage')
    assert response.status_code == 200
    data = response.get_json()
    assert "Python" in data

def test_top_skills(client):
    response = client.get('/api/top-skills')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
    assert len(response.get_json()) == 3

def test_unused_skills(client):
    response = client.get('/api/unused-skills')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
