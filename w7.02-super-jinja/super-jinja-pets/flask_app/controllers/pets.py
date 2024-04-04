from flask_app import app
from flask_app.models.pet import Pet
from flask import render_template, redirect, request


@app.route("/")
@app.route("/pets")
def index():
    """This route displays all pets."""

    pets = Pet.find_all()
    return render_template("index.html", pets=pets)


@app.get("/pets/new")
def new_pet():
    """This route displays the new pet form."""

    return render_template("new_pet.html")


@app.post("/pets/create")
# @app.route("/pets/create", methods=["POST"])
def create_pet():
    """The route that processes the form."""

    print(request.form)
    pet_id = Pet.create(request.form)
    print("THIS IS THE NEW PET'S ID: " + str(pet_id))
    return redirect("/pets")


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
