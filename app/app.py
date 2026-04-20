from flask import Flask
from app.routes.tasks import tasks_bp

app = Flask(__name__)

app.register_blueprint(tasks_bp)

@app.route("/")
def home():
    return "Task Manager API is running 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
