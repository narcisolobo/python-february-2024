from flask_app import app
from flask_app.models.gizmo import Gizmo
from flask import render_template, redirect, request


@app.route("/")
@app.route("/gizmos")
def index():
    """This route displays all gizmos."""

    gizmos = Gizmo.find_all()
    return render_template("index.html", gizmos=gizmos)


@app.get("/gizmos/new")
def new_gizmo():
    """This route displays the new gizmo form."""

    return render_template("new_gizmo.html")


@app.post("/gizmos/create")
def create_gizmo():
    """This route processes the new gizmo form."""

    print(request.form)
    gizmo_id = Gizmo.create(request.form)
    print("THIS IS THE NEW GIZMO'S ID: " + str(gizmo_id))
    return redirect("/gizmos")


@app.get("/gizmos/<int:gizmo_id>")
def gizmo_details(gizmo_id):
    """This route displays the details of one gizmo."""

    gizmo = Gizmo.find_by_id(gizmo_id)
    return render_template("gizmo_details.html", gizmo=gizmo)


@app.get("/gizmos/<int:gizmo_id>/edit")
def edit_gizmo(gizmo_id):
    """This route displays the edit gizmo form."""

    gizmo = Gizmo.find_by_id(gizmo_id)
    return render_template("edit_gizmo.html", gizmo=gizmo)


@app.post("/gizmos/update")
def update_gizmo():
    """This route processes the edit form."""

    gizmo_id = request.form["gizmo_id"]
    Gizmo.update(request.form)
    return redirect(f"/gizmos/{gizmo_id}")


@app.post("/gizmos/<int:gizmo_id>/delete")
def delete_gizmo(gizmo_id):
    """This route deletes a gizmo."""

    Gizmo.delete_by_id(gizmo_id)
    return redirect("/gizmos")
