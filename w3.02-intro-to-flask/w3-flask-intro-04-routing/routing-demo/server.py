from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Handle the request for '/' route."""
    return "This is the root route."


@app.route("/<id>")
def details(id):
    """Handles the details '/id' request."""

    return "Viewing details for id " + id


@app.route("/multiply/<int:num>")
def multiply(num):
    """Return the product of num times 2."""

    return str(num * 2)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
