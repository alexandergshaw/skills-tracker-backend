import pytest
from backend_app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_welcome(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b"Welcome" in res.data

def test_skills(client):
    res = client.get('/api/skills')
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)

def test_projects(client):
    res = client.get('/api/projects')
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)

def test_skill_usage(client):
    res = client.get('/api/skill-usage')
    data = res.get_json()
    assert isinstance(data, dict)
    assert "Python" in data

def test_top_skills(client):
    res = client.get('/api/top-skills')
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) == 3

def test_unused_skills(client):
    res = client.get('/api/unused-skills')
    data = res.get_json()
    assert isinstance(data, list)
