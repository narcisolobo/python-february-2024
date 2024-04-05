from flask import Blueprint, render_template

bp = Blueprint(
    "admin", __name__, url_prefix="/admin", template_folder="admin_templates"
)


@bp.get("/")
def admin_index():
    return render_template("index.html")
