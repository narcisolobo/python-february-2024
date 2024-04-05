from flask import Flask, redirect
from .main import bp as main
from .admin.blueprint import bp as admin


def create_app():
    """Flask app factory."""

    app = Flask(__name__)

    @app.get("/")
    def index():
        return redirect("/main")

    app.register_blueprint(main)
    app.register_blueprint(admin)

    return app
