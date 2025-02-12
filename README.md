# DevOps Lab - ALB Tasks 1 & 2 🚀

Welcome to my **DevOps Lab Repository**! This repo contains solutions for various tasks related to GitHub, CI/CD automation, and application deployment. Let's get started! 🎯

---
## 🏗 Lab 03 - Setting Up Git and Deploying an App

### Step 1: Create a GitHub Account 🦸‍♂️
If you don't already have a GitHub account, create one at [GitHub](https://github.com/).

### Step 2: Application Development 🖥️
1. Create a folder to store your application.
2. Create a Python script:
   ```bash
   nano app.py
   ```
3. Add the following content:
   ```python
   def main():
       print("Hello, World!")

   if __name__ == "__main__":
       main()
   ```
4. Save and exit (Ctrl + X, then Y).
5. Run the application to test it:
   ```bash
   python app.py
   ```

### Step 3: Install Git on Ubuntu 🐧
```bash
sudo apt update
sudo apt install git
```
Check the installation:
```bash
git --version
```

### Step 4: Create a `.gitignore` File 📂
```bash
nano .gitignore
```
Add:
```
venv/
__pycache__/
*.pyc
```

### Step 5: Initialize Git and Commit 📌
```bash
git init
git add .
git commit -m "Initial commit"
```

### Step 6: Create a GitHub Repository 📤
1. Log in to GitHub.
2. Click `+` > `New Repository`.
3. Name it (e.g., `my-python-app`).
4. Copy the repository URL.

### Step 7: Connect Local Repo to GitHub 🌐
```bash
git remote add origin https://github.com/username/my-python-app.git
git branch -M main
git push -u origin main
```

### Step 8: Verify on GitHub ✅
Refresh your GitHub repository page to check if the files are uploaded.

### Step 9: (Optional) Add a README 📖
```bash
nano README.md
```
Write a brief project description, commit, and push it:
```bash
git add README.md
git commit -m "Added README"
git push
```

### Step 10: (Optional) Set up a `requirements.txt` 📦
If your project uses external libraries:
```bash
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Added requirements file"
git push
```

---
## 🎬 Task 0: Netflix EDA
- Take any Netflix movie dataset.
- Apply **Exploratory Data Analysis (EDA)** & visualization techniques.
- Deploy the dataset & analysis to GitHub.
- Keep a **screenshot** of commands used during deployment.

---
## 🌍 Task 1: Personal Website with GitHub Pages
### Steps:
1. Create a **new repository** named `username.github.io`.
2. Add an `index.html` file for the homepage.
3. (Optional) Add a `style.css` file for styling.
4. Commit & push the files:
   ```bash
   git add .
   git commit -m "Added personal website files"
   git push -u origin main
   ```
5. Go to **Settings > Pages** and select the `main` branch.
6. Your website will be live at `https://username.github.io` 🎉

---
## 🤖 Task 2: Automate Deployment with GitHub Actions
### Create a `.github/workflows/deploy.yml` file:
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
### Deliverables 📌
- GitHub repository with **Flask app** & `.yml` workflow file.

---
## 🎯 Git Cheat Sheet 🛠️
| Command | Description |
|---------|-------------|
| `git fetch origin` | Fetches changes from the remote repository. |
| `git status` | Shows the status of the local repository. |
| `git log origin/main..main` | Shows commits not in the remote branch. |
| `git diff origin/main` | Shows file differences. |
| `git pull origin main` | Fetches and merges changes from the remote. |
| `git branch -r` | Lists all remote branches. |
| `git checkout -b new-branch origin/remote-branch` | Creates a local branch to track a remote branch. |
| `git show commit-hash` | Shows changes made in a specific commit. |
| `git remote -v` | Shows the remote repository URL. |

🚀 **Happy Coding!** 🎉
