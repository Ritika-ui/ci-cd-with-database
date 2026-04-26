# 🚀 Task Manager API

> A fully containerized REST API built with Flask, PostgreSQL, and Nginx — featuring Docker Compose, CI/CD pipeline, and persistent database storage.

🌐 **Live Demo:** https://task-manager-api-f8af.onrender.com

---

## ✨ Features

- Create, view, and delete tasks via REST API
- Reverse proxy using Nginx
- PostgreSQL database with persistent storage
- Multi-container setup with Docker Compose
- Automated CI/CD pipeline with GitHub Actions
- Cloud deployment on Render

---

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Flask (Python) |
| Database | PostgreSQL |
| Proxy | Nginx |
| Containerization | Docker + Docker Compose |
| CI/CD | GitHub Actions |
| Deployment | Render |

---

## 📁 Project Structure

```
├── app/
│   ├── app.py
│   ├── routes/
│   ├── db/
│   └── config/
├── nginx/
├── .github/
│   └── workflows/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ⚙️ Architecture

```
User
 ↓
Nginx (Reverse Proxy) :8080
 ↓
Flask Backend (API) :5000
 ↓
PostgreSQL (Persistent Volume) :5432
```

---

## 🔌 API Endpoints

### Get all tasks
```
GET /tasks
```

### Add a task
```
POST /tasks
```
```json
{
  "title": "learn docker"
}
```

### Delete a task
```
DELETE /tasks/<id>
```

---

## 🐳 Run Locally with Docker

**Build and start containers:**
```bash
docker-compose up -d --build
```

**Stop containers:**
```bash
docker-compose down
```

---

## 💾 Database Persistence

PostgreSQL data is stored in a named Docker volume so it survives container restarts:

```yaml
volumes:
  postgres-data:
```

---

## 🔄 CI/CD Pipeline

Every push to `main` triggers the automated pipeline:

```
GitHub Push → Build Docker Image → Push to Docker Hub → Deploy → Live
```

---

## 🧠 Key Learnings

- Flask REST API development
- Docker multi-container architecture
- Reverse proxy setup with Nginx
- PostgreSQL integration with Flask
- Docker networking between containers
- Data persistence using volumes
- CI/CD automation with GitHub Actions

---

## ⚠️ Notes

- Backend communicates with the database using Docker service name `db` (internal DNS)
- Nginx forwards requests from port `8080` → Flask app on port `5000`
- PostgreSQL data persists across container restarts via Docker volume

---

## 👩‍💻 Author

**Ritika Khadka**

---

⭐ If you found this useful, consider giving it a star on GitHub!
