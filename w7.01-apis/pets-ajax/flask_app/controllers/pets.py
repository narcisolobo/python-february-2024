from flask_app import app
from flask_app.models.pet import Pet
from flask import jsonify, render_template, redirect, request


@app.route("/")
def index():
    """This route redirects to /pets."""

    return redirect("/pets")


@app.route("/pets")
def pets():
    """This route displays all pets and the new pet form."""

    pets = Pet.find_all()
    return render_template("pets.html", pets=pets)


@app.post("/pets/create")
def create_pet():
    """The route that processes the form."""

    print(request.form)
    pet_id = Pet.create(request.form)
    pet = Pet.find_by_id(pet_id)
    return pet.__dict__


@app.get("/pets/<int:pet_id>")
def pet_details(pet_id):
    """This route displays one pet's details."""

    pet = Pet.find_by_id(pet_id)
    if pet == None:
        return "Cannot find pet."

    print(type(pet))
    return render_template("pet_details.html", pet=pet)


@app.get("/pets/<int:pet_id>/edit")
def edit_pet(pet_id):
    """This route displays the edit form."""

    pet = Pet.find_by_id(pet_id)
    if pet == None:
        return "Cannot find pet."
    return render_template("edit_pet.html", pet=pet)


@app.post("/pets/update")
def update_pet():
    """This route processes the edit form."""

    pet_id = request.form["pet_id"]
    Pet.update(request.form)
    return redirect(f"/pets/{pet_id}")


@app.post("/pets/<int:pet_id>/delete")
def delete_pet(pet_id):
    """This route deletes a pet."""

    Pet.delete_by_id(pet_id)
    return redirect("/pets")
