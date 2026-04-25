from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "admin" :
        return "Login Succesfull"
    else:
        return "Login Failed"
    

@app.route("/search")
def search():
    query = request.args.get("q")
    return f"Result for {query}"

if __name__ == "__main__" :
    app.run(debug="true")
        
