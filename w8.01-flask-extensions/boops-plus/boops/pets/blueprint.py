from boops.extensions import db
from boops.pets.model import Pet
from boops.pets.form import PetForm
from flask_login import current_user, login_required
from flask import Blueprint, flash, redirect, render_template, request, url_for

bp = Blueprint("pets", __name__, url_prefix="/pets")


@bp.route("/", methods=["GET", "POST"])
@login_required
def pets():
    """
    GET: Renders the all_pets template and the new pet form.
    POST: Processes the new pet form.
    """

    form = PetForm()
    if request.method == "POST":
        if form.validate_on_submit():
            pet = Pet()
            form.populate_obj(pet)
            pet.user_id = current_user.id
            db.session.add(pet)
            db.session.commit()
            return redirect(url_for("pets.pets"))

    pets = Pet.query.all()
    context = {"current_user": current_user, "pets": pets, "form": form}
    return render_template("/pets/pets.html", **context)


@bp.route("/<int:pet_id>", methods=["GET", "POST"])
@login_required
def show_pet(pet_id):
    """
    GET: Renders the pet details and edit pet form.
    POST: Processes the edit pet form.
    """

    pet: Pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    for boop in pet.boops:
        print(boop.user_id)

    if request.method == "POST":
        if form.validate_on_submit():
            if pet.user_id != current_user.id:
                flash("Unauthorized action.", "danger")
                return redirect(url_for("pets.show_pet", pet_id=pet_id))
            form.populate_obj(pet)
            db.session.add(pet)
            db.session.commit()
            return redirect(url_for("pets.show_pet", pet_id=pet_id))

    context = {"current_user": current_user, "pet": pet, "form": form}
    return render_template("/pets/show_pet.html", **context)


@bp.post("/<int:pet_id>/delete")
@login_required
def delete_pet(pet_id):
    """Deletes a pet."""

    pet: Pet = Pet.query.get_or_404(pet_id)

    if pet.user_id != current_user.id:
        flash("Unauthorized action")
        return redirect(url_for("pets.show_pet", pet_id=pet_id))

    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for("pets.pets"))
