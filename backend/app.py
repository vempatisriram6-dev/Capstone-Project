from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  

APP_ENV = os.getenv("ENV", "dev")

@app.route("/health")
def health():
    return jsonify(status="OK", env=APP_ENV), 200

@app.route("/")
def home():
    return "Backend is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
