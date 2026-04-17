# 🚀 Task Manager API (Docker + CI/CD)

A simple **Flask-based Task Manager API** with full **Dockerization and CI/CD pipeline**, deployed live on the cloud.

---

## 🌐 Live Demo

👉 https://ci-cd-with-database.onrender.com

---

## 📌 Features

* Create tasks ✅
* View all tasks 📋
* Delete tasks ❌
* REST API endpoints
* Dockerized application 🐳
* Automated CI/CD pipeline ⚙️
* Live deployment 🌍

---

## 🧱 Tech Stack

* **Backend:** Flask (Python)
* **Database:** SQLite
* **Containerization:** Docker
* **CI/CD:** GitHub Actions
* **Deployment:** Render

---

## 📁 Project Structure

```
project/
├── app.py
├── requirements.txt
├── Dockerfile
├── nginx/
├── .github/workflows/
```

---

## ⚙️ API Endpoints

### 🔹 Get all tasks

```
GET /tasks
```

---

### 🔹 Add a task

```
POST /tasks
```

**Body:**

```json
{
  "title": "learn devops"
}
```

---

### 🔹 Delete a task

```
DELETE /tasks/<id>
```

---

## 🐳 Run Locally with Docker

### 1. Build image

```
docker build -t taskapp .
```

### 2. Run container

```
docker run -p 5000:5000 taskapp
```

### 3. Open in browser

```
http://localhost:5000/tasks
```

---

## 🔄 CI/CD Pipeline

This project uses GitHub Actions to automate:

* Build Docker image
* Push image to registry
* Deploy application automatically

### Workflow:

```
git push → CI build → Docker image → Deploy → Live app
```

---

## 🧠 Key Learnings

* Containerization using Docker
* Reverse proxy setup with Nginx
* CI/CD pipeline automation
* Cloud deployment
* Backend API development
* Database integration

---

## ⚠️ Note

* SQLite database is currently **temporary (inside container)**
* Data resets on redeploy

👉 Future improvement: Use persistent storage or cloud database

---

## 🚀 Future Improvements

* Add frontend (React)
* Use PostgreSQL database
* Add authentication (login/signup)
* Implement Docker volumes
* Deploy on cloud infrastructure (AWS)

---

## 👩‍💻 Author

**Ritika Khadka**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!!!
