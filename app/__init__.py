from flask import Flask
from flask_cors import CORS

def app_register_blueprints(app):
    """
    Register all blueprints from here
    :param app: Flask App
    :return: None
    """
    from app.api import trivia

    # Register routes
    _blue_prints = [
        (trivia.blueprint.BP, True),
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

    app_register_blueprints(app)

    return app
