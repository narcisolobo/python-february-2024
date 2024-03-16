from flask_app import app
from flask_app.models.record import Record
from flask import render_template, redirect, request


@app.route("/")
@app.route("/records")
def index():
    """This route displays all records."""

    records = Record.find_all()
    return render_template("index.html", records=records)


@app.get("/records/new")
def new_record():
    """This route displays the new record form."""

    return render_template("new_record.html")


@app.post("/records/create")
# @app.route("/records/create", methods=["POST"])
def create_record():
    """The route that processes the form."""

    print(request.form)
    record_id = Record.create(request.form)
    print("THIS IS THE NEW RECORD'S ID: " + str(record_id))
    return redirect("/records")


@app.get("/records/<int:record_id>")
def record_details(record_id):
    """This route displays one record's details."""

    record = Record.find_by_id(record_id)
    if record == None:
        return "Cannot find record."

    print(type(record))
    return render_template("record_details.html", record=record)


@app.get("/records/<int:record_id>/edit")
def edit_record(record_id):
    """This route displays the edit form."""

    record = Record.find_by_id(record_id)
    if record == None:
        return "Cannot find record."
    return render_template("edit_record.html", record=record)


@app.post("/records/update")
def update_record():
    """This route processes the edit form."""

    record_id = request.form["record_id"]
    Record.update(request.form)
    return redirect(f"/records/{record_id}")


@app.post("/records/<int:record_id>/delete")
def delete_record(record_id):
    """This route deletes a record."""

    Record.delete_by_id(record_id)
    return redirect("/records")
