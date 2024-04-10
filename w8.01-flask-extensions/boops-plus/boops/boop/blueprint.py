from boops.extensions import db
from boops.boop.model import Boop
from flask_login import current_user
from flask import Blueprint, redirect, request, url_for

bp = Blueprint("boop", __name__, url_prefix="/boops")


@bp.post("/create")
def create_boop():
    """Boops a pet."""

    user_id = current_user.id
    pet_id = request.form.get("pet_id")
    boop = Boop(user_id=user_id, pet_id=pet_id)

    db.session.add(boop)
    db.session.commit()
    return redirect(url_for("pets.show_pet", pet_id=pet_id))


@bp.post("/delete")
def delete_boop():
    """Unboops a pet."""

    user_id = current_user.id
    pet_id = request.form.get("pet_id")
    boop = Boop.query.filter_by(user_id=user_id, pet_id=pet_id).first()

    db.session.delete(boop)
    db.session.commit()
    return redirect(url_for("pets.show_pet", pet_id=pet_id))
