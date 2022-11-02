import sqlite3
from tkinter.font import names
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/register', methods=["GET", "POST"])
def register():
    name = "unknown"

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        conn.execute('INSERT INTO users (email, password) VALUES (?, ?)',
        (email, password))
        conn.commit()
        conn.close()
        
        
 

    return render_template('index.html', name=name)


@app.route('/login', methods=["GET", "POST"])
def login():
    name = "login"
    if request.method == "POST":
        submittedEmail = request.form["email"]
        submittedPassword = request.form["password"]
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ?",
        (submittedEmail, ))
        rows = c.fetchall()
        #if submittedPassword == rows[password]:
    return render_template('login.html')


def get_db_connection():
    path = "/Users/alicespink/project/database.db"
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    return conn



