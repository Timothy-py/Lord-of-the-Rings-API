# ################################################################################################
from flask import Flask, jsonify
from .config.config import config_dict
import os
from src.auth import auth
from src.characters import characters
from flask_jwt_extended import JWTManager
from src.constants.http_status_codes import HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK
from src.favorites import favorites
from src.model import db
from flasgger import Swagger, swag_from
from src.config.swagger import template, swagger_config

# ################################################################################################


def create_app(config=config_dict['testing']):

    # instantiate the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config)

    # connect the database
    db.app = app
    db.init_app(app)

    # initialize jwt manager
    JWTManager(app=app)

    # register app handlers
    app.register_blueprint(auth)
    app.register_blueprint(characters)
    app.register_blueprint(favorites)

    # configure swagger
    Swagger(app, config=swagger_config, template=template)

    # api index route
    @app.get('/')
    @swag_from('./docs/index.yaml')
    def index():
        return jsonify({
            'message': 'LORD OF THE RINGS CHARACTERS API'
        }), HTTP_200_OK

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
