# 🚀 Task Manager API (Docker + Flask + PostgreSQL + Nginx + CI/CD)

A fully containerized **Task Manager REST API** built using Flask, PostgreSQL, and Nginx with Docker Compose, including CI/CD deployment and persistent database storage.

---

## 🌐 Live Demo

👉 https://ci-cd-with-database-1.onrender.com

---

## 📌 Features

* Create tasks ✅
* View all tasks 📋
* Delete tasks ❌
* REST API (Flask)
* Reverse proxy using Nginx 🔁
* PostgreSQL database 🗄️ 
* Persistent storage using Docker volumes 💾
* Multi-container setup 🐳
* CI/CD pipeline ⚙️ 
* Cloud deployment 🌍

---

## 🧱 Tech Stack

* **Backend:** Flask (Python)
* **Database:** PostgreSQL
* **Proxy:** Nginx
* **Containerization:** Docker + Docker Compose
* **CI/CD:** GitHub Actions
* **Deployment:** Render / Cloud

---

## 📁 Project Structure

project/
│
├── app/
│   ├── __init__.py
│   ├── app.py                  # Flask entry point (main backend)
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   └── tasks.py           # API routes (GET, POST tasks)
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   └── database.py        # PostgreSQL connection logic
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py          # Environment variables / settings
│
├── nginx/
│   └── nginx.conf             # Reverse proxy configuration
│
├── Dockerfile                 # Builds Flask app container
├── docker-compose.yml         # Multi-container setup (app + nginx + db)
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── .github/
│   └── workflows/
│       └── ci.yml             # CI pipeline (GitHub Actions)
---

## ⚙️ Architecture

```text
User
 ↓
Nginx (Reverse Proxy)
 ↓
Flask Backend (API)
 ↓
PostgreSQL (Persistent Volume)

🔌 API Endpoints

🔹 Get all tasks
   GET /tasks
🔹 Add a task
   POST /tasks

JSON
{
  "title": "learn docker"
}
🔹 Delete a task
   DELETE /tasks/<id>

🐳 Run Locally with Docker

1. Build and start containers
docker-compose up -d --build

2. Stop containers
docker-compose down


💾 Database Persistence

This project uses Docker volumes to persist PostgreSQL data:

volumes:
  postgres-data:

✔ Data remains even after container restart


🔄 CI/CD Pipeline

Automates deployment using GitHub Actions:

GitHub push → Build Docker image → Deploy → Live update

🧠 Key Learnings
-> Flask REST API development
-> Docker multi-container architecture
-> Reverse proxy using Nginx
-> PostgreSQL integration
-> Docker networking
-> Data persistence using volumes
-> CI/CD automation


⚠️ Notes
-> Backend communicates with DB using Docker service name (db)
-> Nginx forwards requests from port 8080 → Flask app
-> PostgreSQL runs in a persistent Docker volume


👩‍💻 Author

Ritika Khadka


⭐ If you like this project

If you found this useful, please consider giving it a ⭐ on GitHub!
