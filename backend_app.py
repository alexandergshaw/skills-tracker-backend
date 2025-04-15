from flask import Flask, jsonify
from collections import Counter

# Static skill and project data
skills = [
    {"name": "Python", "experience": 3},
    {"name": "Flask", "experience": 2},
    {"name": "SQL", "experience": 2},
    {"name": "HTML", "experience": 4},
    {"name": "CSS", "experience": 4},
    {"name": "JavaScript", "experience": 3},
    {"name": "Git", "experience": 5},
    {"name": "API", "experience": 2}
]

projects = [
    {"title": "Portfolio Website", "tech": "HTML, CSS, JavaScript"},
    {"title": "Todo App", "tech": "Python, Flask, SQL, HTML, CSS"},
    {"title": "Weather Dashboard", "tech": "Python, Flask, API, JavaScript, HTML, CSS"},
    {"title": "Blog CMS", "tech": "Flask, SQL, HTML, CSS"},
    {"title": "Git Practice Project", "tech": "Python, Git"},
    {"title": "API Data Visualizer", "tech": "Python, API, JavaScript"}
]

# App factory pattern
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def welcome():
        return jsonify(message="Welcome to the Skills Tracker Backend API!")

    @app.route('/api/skills')
    def get_skills():
        return jsonify(skills)

    @app.route('/api/projects')
    def get_projects():
        return jsonify(projects)

    @app.route('/api/skill-usage')
    def get_skill_usage():
        usage_count = Counter()
        for project in projects:
            for skill in skills:
                if skill["name"].lower() in project["tech"].lower():
                    usage_count[skill["name"]] += 1
        return jsonify(dict(usage_count))

    @app.route('/api/top-skills')
    def get_top_skills():
        usage_count = Counter()
        for project in projects:
            for skill in skills:
                if skill["name"].lower() in project["tech"].lower():
                    usage_count[skill["name"]] += 1
        top_skills = usage_count.most_common(3)
        return jsonify(top_skills)

    @app.route('/api/unused-skills')
    def get_unused_skills():
        used = set()
        for project in projects:
            for skill in skills:
                if skill["name"].lower() in project["tech"].lower():
                    used.add(skill["name"])
        unused = [skill for skill in skills if skill["name"] not in used]
        return jsonify(unused)

    return app

# Only run server when executed directly
if __name__ == '__main__':
    import os
    app = create_app()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
