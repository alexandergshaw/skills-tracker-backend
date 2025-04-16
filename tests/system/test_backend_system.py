import pytest
from backend_app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_root_route_returns_200_and_json(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.is_json
    assert "message" in response.get_json()

def test_skills_returns_all_expected_keys(client):
    response = client.get('/api/skills')
    skills = response.get_json()
    assert isinstance(skills, list)
    for skill in skills:
        assert "name" in skill and "experience" in skill

def test_projects_returns_all_expected_keys(client):
    response = client.get('/api/projects')
    projects = response.get_json()
    assert isinstance(projects, list)
    for project in projects:
        assert "title" in project and "tech" in project

def test_skill_usage_returns_valid_counts(client):
    response = client.get('/api/skill-usage')
    usage = response.get_json()
    assert isinstance(usage, dict)
    assert all(isinstance(k, str) and isinstance(v, int) for k, v in usage.items())

def test_top_skills_has_exactly_three(client):
    response = client.get('/api/top-skills')
    top = response.get_json()
    assert isinstance(top, list)
    assert len(top) == 3
    for item in top:
        assert isinstance(item, list) and len(item) == 2
        assert isinstance(item[0], str) and isinstance(item[1], int)

def test_unused_skills_structure_is_valid(client):
    response = client.get('/api/unused-skills')
    unused = response.get_json()
    assert isinstance(unused, list)
    for skill in unused:
        assert "name" in skill and "experience" in skill
