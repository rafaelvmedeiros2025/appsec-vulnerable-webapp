from flask import Flask, request
import sqlite3
from db import init_db

app = Flask(__name__)

init_db()

@app.route("/")
def home():
    return "AppSec Vulnerable App"

@app.route("/login")
def login():

    username = request.args.get("username")
    password = request.args.get("password")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    result = cursor.execute(query).fetchone()

    conn.close()

    if result:
        return "Logged in!"
    else:
        return "Invalid credentials"

if __name__ == "__main__":
    app.run(debug=True)