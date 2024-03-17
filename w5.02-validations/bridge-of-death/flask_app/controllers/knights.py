from flask_app import app
from flask import redirect, render_template


@app.get("/")
def index():
    """This route redirects the user to /knights/new."""

    return redirect("/knights/new")


@app.get("/knights/new")
def new_knight():
    """This route displays the bridge of death form."""

    return render_template("index.html")
