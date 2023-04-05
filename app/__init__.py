from flask import Flask
from flask_cors import CORS
from app.firebase.connect import init_db

def app_register_blueprints(app):
    """
    Register all blueprints from here
    :param app: Flask App
    :return: None
    """
    from app.api import trivia, scrape

    # Register routes
    _blue_prints = [
        (trivia.blueprint.BP, True),
        (scrape.blueprint.BP, True),
    ]
    for _bp, include, in _blue_prints:
        if include:
            app.register_blueprint(_bp)


def create_app():
    """
    create and configure the app
    """
    app = Flask(__name__)
    CORS(app)
    with app.app_context():
        init_db()

    app_register_blueprints(app)

    return app
