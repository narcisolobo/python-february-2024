from flask import Flask
from marvel.main.blueprint import bp as main


def create_app():
    """Flask app factory."""

    app = Flask(__name__)

    # blueprints
    app.register_blueprint(main)
    app.secret_key = "ca83d1c46629d8793890a30650acf1b63960fe459228a3cc7455d8e5bb1adb32"

    return app
