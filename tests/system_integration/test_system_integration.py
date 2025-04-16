import requests

# Replace this with your actual deployed API root
BASE_URL = "https://skills-tracker-backend.onrender.com"

def test_api_is_up():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert "Welcome" in response.json()["message"]

def test_skills_api_returns_valid_structure():
    response = requests.get(f"{BASE_URL}/api/skills")
    data = response.json()
    assert isinstance(data, list)
    for skill in data:
        assert "name" in skill and "experience" in skill

def test_projects_api_returns_valid_structure():
    response = requests.get(f"{BASE_URL}/api/projects")
    data = response.json()
    assert isinstance(data, list)
    for project in data:
        assert "title" in project and "tech" in project

def test_skill_usage_api_matches_skills():
    usage_res = requests.get(f"{BASE_URL}/api/skill-usage")
    skills_res = requests.get(f"{BASE_URL}/api/skills")

    usage = usage_res.json()
    skills = [s["name"] for s in skills_res.json()]
    for skill in usage:
        assert skill in skills
        assert isinstance(usage[skill], int)

def test_top_skills_and_skill_usage_are_consistent():
    top_res = requests.get(f"{BASE_URL}/api/top-skills")
    usage_res = requests.get(f"{BASE_URL}/api/skill-usage")

    top = top_res.json()
    usage = usage_res.json()

    # Get the top 3 by usage count (as list of lists)
    sorted_usage = sorted(usage.items(), key=lambda x: x[1], reverse=True)[:3]
    sorted_usage_as_lists = [list(item) for item in sorted_usage]

    assert set(tuple(skill) for skill in top) == set(tuple(skill) for skill in sorted_usage_as_lists)
    top_res = requests.get(f"{BASE_URL}/api/top-skills")
    usage_res = requests.get(f"{BASE_URL}/api/skill-usage")

    top = top_res.json()
    usage = usage_res.json()

    sorted_usage = sorted(usage.items(), key=lambda x: x[1], reverse=True)[:3]
    sorted_usage_as_lists = [list(item) for item in sorted_usage]

    assert top == sorted_usage_as_lists

def test_unused_skills_not_in_usage():
    unused_res = requests.get(f"{BASE_URL}/api/unused-skills")
    usage_res = requests.get(f"{BASE_URL}/api/skill-usage")

    unused = unused_res.json()
    used_skills = usage_res.json().keys()

    for skill in unused:
        assert skill["name"] not in used_skills
