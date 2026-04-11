from flask import Flask
from flask_talisman import Talisman


app = Flask(__name__)
Talisman(app) # This adds CSP, HSTS, and other headers ZAP is looking for


@app.route("/")
def home():
    return "Flask app is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    

