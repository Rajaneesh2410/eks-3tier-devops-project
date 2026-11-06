from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import psycopg2

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"]
    )

@app.route("/")
def home():
    return jsonify({
        "message": "Employee Management API is running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/employees", methods=["GET"])
def get_employees():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, role FROM employees ORDER BY id")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify([
        {"id": row[0], "name": row[1], "role": row[2]}
        for row in rows
    ])

@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO employees (name, role) VALUES (%s, %s) RETURNING id",
        (data["name"], data["role"])
    )
    employee_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"id": employee_id, "message": "Employee added"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
