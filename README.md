# Skills Tracker Backend API (Flask)

This Flask-based backend powers the **Skills Tracker** app. It serves a list of skills and projects via API endpoints and provides insights like skill usage frequency and unused skills. It is designed to pair with a frontend Flask or JavaScript app.

---

## Live Demo (after deployment)
> Replace this with your actual URL once deployed  
https://your-backend.onrender.com/api/skills

---

## Features

- Serve a list of **skills** and **projects** in JSON format
- Compute frequency of skill usage across projects
- Return top 3 most-used skills
- Identify unused skills

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/skills-backend.git
cd skills-backend
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install dependencies
```bash
python backend_app.py
```

---

## Deploy to Render (Free Hosting)

Follow these steps to deploy the Flask backend to [Render](https://render.com):

### 1. Prepare your project

Make sure your project includes the following files:
- `backend_app.py` (your main Flask app)
- `requirements.txt` (with `Flask` and `pytest`)
- `Procfile` (to tell Render how to run your app)

Your `Procfile` should contain:
```
web: python backend_app.py
```

### 2. Push your project to GitHub

Initialize a Git repo if you haven’t already:

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/skills-backend.git
git push -u origin main
```

> Replace `yourusername` with your actual GitHub username.

---

### 3. Create a new Web Service on Render

1. Go to https://render.com
2. Click **“New +”** → **“Web Service”**
3. Connect your GitHub account and select your repo

---

### 4. Configure Render settings

| Setting             | Value                        |
|---------------------|------------------------------|
| Name                | `skills-backend` (or similar) |
| Environment         | Python                       |
| Build Command       | *(leave blank)*              |
| Start Command       | `python backend_app.py`      |
| Region              | United States (or closest)   |
| Instance Type       | Free                         |

---

### 5. Deploy

Click **"Create Web Service"**.  
Render will install your dependencies, start the server, and give you a public URL like:

```
https://skills-backend.onrender.com
```

You can now make requests to your API endpoints from a frontend or Postman!

