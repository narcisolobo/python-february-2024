from flask import Flask, render_template, session
from dotenv import load_dotenv
from os import environ

load_dotenv()

app = Flask(__name__)
app.secret_key = environ.get("SECRET_KEY")


@app.route("/")
def index():
    if "counter" not in session:
        session["counter"] = 0
    session["counter"] += 1
    session["username"] = "kermit"
    session["email"] = "kermit@thefrog.com"
    print(environ.get("API_KEY"))
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5500)
