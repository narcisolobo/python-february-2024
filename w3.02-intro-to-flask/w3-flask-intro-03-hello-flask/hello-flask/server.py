from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """This view function handles the root route."""

    return "You're at the root route."


@app.route("/about")
def about():
    """This view function handles the /about route."""

    return "You're at the /about route."


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
