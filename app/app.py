from flask import Flask, jsonify, request
import os

app = Flask(__name__)


# Add this function in app.py
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS health_checks (
            id SERIAL PRIMARY KEY,
            url TEXT NOT NULL,
            status TEXT NOT NULL,
            last_checked TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

# Call it when app starts (before first route)
init_db()
@app.route("/")
def home():
    return "App is running 🚀"


@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return "Use POST with JSON"

    data = request.get_json()

    if not data or "user" not in data:
        return {"error": "Missing user"}, 400

    return {"message": f"Hello {data['user']}"}

@app.route("/config")
def config():
    debug_mode = os.environ.get("DEBUG_MODE")
    if debug_mode == "True":
        return "Debugging is ON"
    return 100 / 0


@app.route("/secret")
def secret():
    return os.environ.get("API_KEY")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
