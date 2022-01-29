from flask import Flask, jsonify
import os
from src.auth import auth
from src.characters import characters
from flask_jwt_extended import JWTManager
from src.constants.http_status_codes import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from src.favorites import favorites
from src.model import db


def create_app(test_config=None):

    # instantiate the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
            SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DB_URI'),
            SQLALCHEMY_TRACK_MODIFICATIONS=False
        )
    else:
        app.config.from_mapping(test_config)

    # connect the database
    db.app = app
    db.init_app(app)

    # initialize jwt manager
    JWTManager(app=app)

    # register app handlers
    app.register_blueprint(auth)
    app.register_blueprint(characters)
    app.register_blueprint(favorites)

    # api index route

    @app.get('/')
    def index():
        return jsonify({
            'message': 'LORD OF THE RINGS CHARACTERS API'
        }), 200

    # 404 error handler
    @app.errorhandler(HTTP_404_NOT_FOUND)
    def handle_404(e):
        return jsonify({
            'error': 'Route Does Not Exist',
        }), HTTP_404_NOT_FOUND

    # 500 error handler
    @app.errorhandler(HTTP_500_INTERNAL_SERVER_ERROR)
    def handle_500(e):
        return jsonify({
            'error': 'Something went wrong with the server'
        }), HTTP_500_INTERNAL_SERVER_ERROR

    return app
