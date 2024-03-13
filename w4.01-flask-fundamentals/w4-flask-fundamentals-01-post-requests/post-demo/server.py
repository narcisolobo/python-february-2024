from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "76b0cae084f7f59aca1a3e1c68b8b42f6ab3995535fb395814e1a2c66eaa87d8"


@app.route("/play")
def index():
    """The route that displays the form."""
    return render_template("index.html")


@app.post("/process")
def process():
    """The route that processes the form."""
    print("USERNAME: ", request.form["username"])
    print("EMAIL: ", request.form["email"])

    session["username"] = request.form["username"]
    session["email"] = request.form["email"]
    return redirect("/results")


@app.get("/results")
def results():
    """The route that displays the results."""
    print(session["username"])
    print(session["email"])
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)
