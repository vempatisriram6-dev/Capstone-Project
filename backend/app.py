from flask import Flask, jsonify
from flask_cors import CORS
import os
import psycopg2

app = Flask(__name__)
CORS(app)  

# Root route
@app.route("/")
def home():
    return jsonify({
        "status": "Backend is running"
    })

# Health check route
@app.route("/health")
def health():
    return jsonify({
        "status": "OK",
        "env": os.getenv("ENV", "dev")
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
