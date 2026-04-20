from flask import Blueprint, request, jsonify
from app.db.database import get_connection

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    conn.close()
    return jsonify(tasks)


@tasks_bp.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    title = data.get("title")

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    conn.commit()
    conn.close()

    return {"message": "Task added"}
