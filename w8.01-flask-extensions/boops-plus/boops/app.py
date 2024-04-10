from os import environ
from .filters import age
from flask_login import current_user
from .auth.blueprint import bp as auth
from .boop.blueprint import bp as boop
from .main.blueprint import bp as main
from .pets.blueprint import bp as pets
from flask import Flask, render_template
from .extensions import bcrypt, db, login_manager, migrate

MYSQL_PASSWORD = environ.get("MYSQL_PASSWORD")
MYSQL_CONNECTION_STRING = (
    f"mysql+pymysql://root:{MYSQL_PASSWORD}@localhost:3306/boops_plus_db"
)


def create_app():
    """Flask app factory."""

    app = Flask(__name__)

    # configurations
    app.secret_key = environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = MYSQL_CONNECTION_STRING

    # initialize extensions
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    app.register_blueprint(auth)
    app.register_blueprint(boop)
    app.register_blueprint(main)
    app.register_blueprint(pets)

    # custom 404 page
    @app.errorhandler(404)
    def not_found(err):
        """Custom 404 page."""

        context = {"current_user": current_user, "err": err}
        return render_template("/main/404.html", **context)

    # age template filter
    app.add_template_filter(age)

    return app
