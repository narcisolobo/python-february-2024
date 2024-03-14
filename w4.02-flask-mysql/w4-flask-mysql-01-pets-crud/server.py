from flask import Flask, redirect, render_template, request
from pet import Pet

app = Flask(__name__)


@app.route("/")
@app.route("/pets")
def index():
    """This route displays all pets."""

    pets = Pet.find_all()
    return render_template("index.html", pets=pets)


@app.route("/pets/new")
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


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5500)
