from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.knight import Knight


@app.get("/")
def index():
    """This route redirects the user to /knights/new."""

    return redirect("/knights/new")


@app.get("/knights/new")
def new_knight():
    """This route displays the bridge of death form."""

    return render_template("index.html")


@app.post("/knights/create")
def create_knight():
    """This route processes the bridge of death form."""

    if not Knight.form_is_valid(request.form):
        return redirect("/knights/new")
    return redirect("/")
