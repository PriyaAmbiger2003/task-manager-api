# Task Manager API (Django + JWT)

A RESTful API for managing tasks with JWT authentication using Django REST Framework.


# Project Setup Instructions

## 1. Clone Repository

git clone https://github.com/PriyaAmbiger2003/task-manager-api.git
cd task-manager-api

## 2. Create Virtual Environment

python -m venv env
env\Scripts\activate

## 3. Install Dependencies

pip install -r requirements.txt

## 4. Run Migrations

python manage.py makemigrations
python manage.py migrate

## 5. Run Server

python manage.py runserver

Server will run at: http://127.0.0.1:8000/

---

# JWT Authentication

## Register

POST /api/register/

Body:
{
"name": "Priya",
"email": "[priya@gmail.com](mailto:priya@gmail.com)",
"password": "123456"
}

---

## Login

POST /api/login/

Response:
{
"access": "token",
"refresh": "token"
}

---

## Use Token

Add header in all protected APIs:

Authorization: Bearer <access_token>

---

## Refresh Token

POST /api/token/refresh/

---

# 📋 API Documentation

## Task APIs

POST /api/tasks/ → Create task
GET /api/tasks/ → Get all tasks
GET /api/tasks/{id}/ → Get single task
PUT /api/tasks/{id}/ → Update task
DELETE /api/tasks/{id}/ → Delete task

---

## Custom APIs

GET /api/tasks/my_tasks/
GET /api/tasks/assigned_tasks/

---

# 🔍 Filtering & Search

/api/tasks?status=completed
/api/tasks?priority=high
/api/tasks?search=project

---

# Permissions

* Only creator can delete task
* Assigned user can update task
* Other users cannot modify

---

#  Validations

* Due date cannot be in the past
* Title cannot be empty
* Assigned user must exist

---

#  Steps to Test JWT Authentication

1. Register user
2. Login to get access token
3. Copy access token
4. Add Authorization header
5. Call protected APIs

---

# Postman Collection

Import provided JSON collection and test APIs.

---

# Bonus Features

* Filtering & search
* Custom permissions
* Clean API structure

---

# 👩‍💻 Author

Priya Ambiger
