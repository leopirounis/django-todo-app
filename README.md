# 📝 Django To-Do List App

A simple to-do list web application built with Django. Users can register, log in, add tasks, mark them as complete, and delete them.

---

## 🚀 Features

- User registration and login 🔐
- Add tasks ✅
- Mark tasks as complete or undo 🔁
- Delete tasks 🗑
- Each user sees only their own tasks 👤

---

## 🛠 Tech Stack

- Python 🐍
- Django 🧱
- HTML 🎨
- SQLite (default dev database)

---

## 🧑‍💻 Installation (Local)

1. **Clone the repo**  
   ```bash
   git clone https://github.com/leopirounis/django-todo-app.git
   cd django-todo-app

2. **Create a virtual environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate      # On Windows: venv\Scripts\activate
    
3. **Install dependencies**
     ```bash
     pip3 install -r requirements.txt
     
4. **Set up environment variables** \
   Create a .env file in the project root:
   ```bash
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   
5. **Run migrations**
    ```bash
    python3 manage.py migrate

6. **Run The server**
    ```bash
    python3 manage.py runserver

## 👤 User Accounts
Visit /register/ to create a new user.

After logging in, you'll only see and manage your own tasks.

## 📦 Requirements \
To install required packages:
```bash
pip3 install -r requirements.txt
