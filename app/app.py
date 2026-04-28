from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "App is running 🚀"


@app.route("/data", methods=["POST"])
def data():
    user = request.json["user"]
    return jsonify({"message": f"Hello {user}"})

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
