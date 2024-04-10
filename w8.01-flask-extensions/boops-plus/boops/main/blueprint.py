from flask import Blueprint, render_template
from flask_login import current_user

bp = Blueprint("main", __name__)


@bp.get("/")
def index():
    """Renders the landing page."""

    context = {"current_user": current_user}
    return render_template("/main/index.html", **context)
