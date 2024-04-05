from flask import Blueprint

bp = Blueprint("main", __name__, url_prefix="/main")


@bp.get("/")
def main_index():
    return "Flask main blueprint"


@bp.get("/about")
def main_about():
    return "Main about route"
