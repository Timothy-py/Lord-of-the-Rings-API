from flask import Flask, jsonify
import os
from src.auth import auth
from src.characters import characters
from src.favorites import favorites


def create_app(test_config=None):

    # instantiate the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY")
        )
    else:
        app.config.from_mapping(test_config)

    @app.get('/')
    def index():
        return jsonify({
            'message': 'LORD OF THE RINGS CHARACTERS API'
        }), 200

    # register app handlers
    app.register_blueprint(auth)
    app.register_blueprint(characters)
    app.register_blueprint(favorites)

    return app
