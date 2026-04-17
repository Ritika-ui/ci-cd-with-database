from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DB = "tasks.db"

# Create table if not exists
def init_db():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Get all tasks
@app.route("/")
def home():
    return "Task Manager API is running 🚀"

@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()

    return jsonify(tasks)

# Add a task
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    title = data.get("title")

    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()

    return {"message": "Task added!"}
# Delete a task
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return {"message": "Task deleted!"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
