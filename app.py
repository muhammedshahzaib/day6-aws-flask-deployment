import os
from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Extract parameters dynamically from Environment Variables
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER", "admin")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "flaskdb")

@app.route("/")
def home():
    return "Day 6 AWS Flask Deployment is running perfectly on EC2!"

@app.route("/health")
def health():
    return "OK"

@app.route("/db-test")
def db_test():
    try:
        # Establish connection dynamically using current runtime environment config
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            connect_timeout=5
        )
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION();")
        db_version = cursor.fetchone()
        cursor.close()
        conn.close()
        return jsonify({
            "status": "Success",
            "message": f"Connected to RDS MySQL successfully! DB Version: {db_version[0]}"
        })
    except Exception as e:
        return jsonify({
            "status": "Error",
            "message": f"Failed to connect to database: {str(e)}"
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

