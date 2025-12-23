import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Environment variables
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
APP_ENV = os.getenv("ENV", "dev")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

# ✅ Basic health check (NO DB)
@app.route("/health")
def health():
    return jsonify(status="OK", env=APP_ENV), 200


# ✅ DB health check (OPTIONAL)
@app.route("/health/db")
def health_db():
    try:
        conn = get_db_connection()
        conn.close()
        return jsonify(status="OK", db="connected"), 200
    except Exception as e:
        return jsonify(status="ERROR", error=str(e)), 500


@app.route("/users")
def users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
