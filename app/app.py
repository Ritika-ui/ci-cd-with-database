from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection
conn = psycopg2.connect(
    os.environ.get("DATABASE_URL""),
    sslmode="require"
)
cur = conn.cursor()

# Create table if not exists
def init_db():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL
        )
    """)
    conn.commit()

init_db()

# Home route
@app.route("/")
def home():
    return "Task Manager API is running 🚀"

# Get all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()

    # Convert tuples to JSON-friendly format
    task_list = [{"id": t[0], "title": t[1]} for t in tasks]

    return jsonify(task_list)

# Add a task
@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    title = data.get("title")

    cur.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    conn.commit()

    return {"message": "Task added!"}

# Delete a task
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    cur.execute("DELETE FROM tasks WHERE id = %s", (id,))
    conn.commit()

    return {"message": "Task deleted!"}

# Run app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
