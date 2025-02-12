# DevOps Lab Repository

## Lab 03: Git & GitHub on EC2 Ubuntu Instance

This repository contains the tasks for my DevOps lab, completed using an EC2 Ubuntu instance. Below are the steps I followed to set up Git, deploy an application, and automate deployments using GitHub Actions.

---

## 🔹 Setting Up Git on EC2 Ubuntu Instance

### Step 1: Update and Install Git
```bash
sudo apt update
sudo apt install git
```
Verify installation:
```bash
git --version
```

### Step 2: Configure Git
```bash
git config --global user.name "Saad"
git config --global user.email "your-email@example.com"
```

---

## 🔹 Application Development & Deployment

### Step 1: Create the Application
Inside the home directory:
```bash
mkdir dnetflix-task && cd dnetflix-task
nano app.py
```
Paste the following:
```python
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
```
Save and exit (Ctrl + X, then Y).

Run to verify:
```bash
python3 app.py
```

### Step 2: Initialize Git & Create `.gitignore`
```bash
git init
nano .gitignore
```
Add:
```
venv/
__pycache__/
*.pyc
```
Save and exit.

Stage and commit:
```bash
git add .
git commit -m "Initial commit"
```

### Step 3: Create & Connect GitHub Repository
```bash
git remote add origin https://github.com/saadhaniftaj/DevOps_lab2_app.git
```
Push changes:
```bash
git branch -M main
git push -u origin main
```

If authentication fails, use a personal access token instead of a password.

---

## 🔹 Task 0: Netflix EDA Deployment
Performed Exploratory Data Analysis (EDA) on a Netflix dataset and uploaded it to GitHub.

1. Ran analysis in Jupyter Notebook.
2. Saved results and visualizations.
3. Pushed the project to GitHub:
   ```bash
   git add .
   git commit -m "Added Netflix EDA"
   git push -u origin main
   ```

---

## 🔹 Task 01: Hosting a Personal Website Using GitHub Pages

1. Created a repository `saadhaniftaj.github.io` on GitHub.
2. Created an `index.html` file:
   ```bash
   nano index.html
   ```
   Sample content:
   ```html
   <html>
   <head><title>My Website</title></head>
   <body><h1>Welcome to My Personal Website!</h1></body>
   </html>
   ```
3. Added, committed, and pushed files:
   ```bash
   git add .
   git commit -m "Added personal website"
   git push -u origin main
   ```
4. Activated GitHub Pages in repository settings.

Live URL: `https://saadhaniftaj.github.io`

---

## 🔹 Task 02: Automating Deployment with GitHub Actions

### Step 1: Create `.github/workflows/deploy.yml`
```bash
mkdir -p .github/workflows
nano .github/workflows/deploy.yml
```
Add the following:
```yaml
name: Deploy Application

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run application
        run: |
          python app.py &
```

### Step 2: Commit and Push
```bash
git add .
git commit -m "Added GitHub Actions workflow"
git push -u origin main
```
The application will now deploy automatically on every push.

---

## 🔹 Useful Git Commands

| Command | Description |
|---------|-------------|
| `git status` | Shows the status of your local repository. |
| `git log --oneline` | Displays commit history in a compact format. |
| `git pull origin main` | Fetches and merges remote changes. |
| `git remote -v` | Shows the remote repository URL. |

---

🔥 **This repo documents my DevOps Lab journey!** 🚀
