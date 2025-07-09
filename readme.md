# Django JWT Auth API - Signup/Login

This project provides a **Django REST API** for user authentication (Signup, Login, Me API) using **JWT**. It includes support for **local development** via `venv` and **containerized deployment** using **Docker + Docker Compose**.

---

## 📦 Tech Stack

- **Backend:** Django, Django REST Framework
- **Auth:** JWT (via `djangorestframework-simplejwt`)
- **API Docs:** Swagger (`drf-yasg`)
- **Containerization:** Docker, Docker Compose
- **Env Config:** python-dotenv

---

## 📂 Features

- User Signup with custom fields (`phone`)
- JWT-based Login (`/api/login/`)
- Get current logged-in user (`/api/me/`)
- Swagger documentation at `/swagger/`
- Superuser and Django Admin Panel (`/admin/`)
- Supports both **local (venv)** and **Docker** environments

---

## 🔧 Dependencies

Installed via `pip` and listed in `requirements.txt`:

```txt
Django
djangorestframework
djangorestframework-simplejwt
drf-yasg
python-dotenv
```

## 🚀 Getting Started

### 🔁 Option 1: Run Locally using Virtual Environment

#### 1. Clone the Repository

```bash
git clone https://github.com/hunain-parekh/aak-task-backend.git
cd aak-task-backend
```

#### 2. Setup Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Requirements

```bash
pip install -r requirements.txt
```

#### 4. Run Migrations and Start Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # Optional
python manage.py runserver
```

### 🐳 Option 2: Run with Docker

#### 1. Clone the Repository

```bash
git clone https://github.com/hunain-parekh/aak-task-backend.git
cd aak-task-backend
```

#### 2. Build Docker Image & Start Services

```bash
docker-compose build
docker-compose up
```

#### 3. Apply Migrations & Create Superuser

```bash
docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

#### ✅ App Running at:

- Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- Admin Panel: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## 🔐 API Endpoints

| Endpoint            | Method | Auth Required | Description         |
| ------------------- | ------ | ------------- | ------------------- |
| `/api/auth/signup/` | POST   | ❌ No         | Register a new user |
| `/api/auth/login/`  | POST   | ❌ No         | Get JWT token       |
| `/api/auth/me/`     | GET    | ✅ Yes        | Get current user    |

## ✍️ Author

- **Name:** Hunain Parekh
- **GitHub:** [github.com/hunain-parekh](https://github.com/hunain-parekh)
- **Email:** hunainparekh85@gmail.com

---

## 📝 Assigned By

- **Name:** AAK Team
- **Role:** Task Assignment for Auth Backend
- **Date:** 08 July 2025
