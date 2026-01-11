from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE,
            address TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        name = request.form["name"]
        address = request.form["address"]

        try:
            conn = sqlite3.connect("data.db")
            cur = conn.cursor()
            cur.execute("INSERT INTO users (name, address) VALUES (?, ?)", (name, address))
            conn.commit()
            conn.close()
            message = "Data stored successfully!"
        except:
            message = "Name already exists!"

    return render_template("index.html", message=message)

@app.route("/search", methods=["GET", "POST"])
def search():
    result = ""
    if request.method == "POST":
        name = request.form["name"]

        conn = sqlite3.connect("data.db")
        cur = conn.cursor()
        cur.execute("SELECT address FROM users WHERE name = ?", (name,))
        row = cur.fetchone()
        conn.close()

        if row:
            result = f"Address: {row[0]}"
        else:
            result = "Not Exist"

    return render_template("search.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
