from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    API_KEY = "12345SECRET"
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "admin" :
        return "Login Succesfull"
    else:
        return "Login Failed"
    
@app.route("/user")
def user():
    name = request.args.get("name")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE name = '" + name + "'"
    cursor.execute(query)

    return str(cursor.fetchall())


@app.route("/search")
def search():
    query = request.args.get("q")
    return f"Result for {query}"

if __name__ == "__main__" :
    app.run(host="0.0.0.0", port=5000)        
