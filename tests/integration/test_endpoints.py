import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from backend_app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_root_welcome_message(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_json()["message"].startswith("Welcome")

def test_skills_list_returns_array(client):
    response = client.get('/api/skills')
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert all("name" in skill and "experience" in skill for skill in data)

def test_projects_list_returns_array(client):
    response = client.get('/api/projects')
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert all("title" in project and "tech" in project for project in data)

def test_skill_usage_counts_match_expected(client):
    response = client.get('/api/skill-usage')
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, dict)
    assert "Python" in data
    assert isinstance(data["Python"], int)
    assert data["Python"] > 0

def test_top_skills_returns_three_items(client):
    response = client.get('/api/top-skills')
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 3
    for item in data:
        assert isinstance(item, list) and len(item) == 2  # (skill, count)

def test_unused_skills_returns_valid_subset(client):
    response = client.get('/api/unused-skills')
    data = response.get_json()
    assert response.status_code == 200
    assert isinstance(data, list)
    for skill in data:
        assert "name" in skill and "experience" in skill
