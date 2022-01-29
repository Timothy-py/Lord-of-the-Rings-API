from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash
import validators

from src.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT

from src.model import User, db
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity


# configure authentication route
auth = Blueprint('auth', __name__, url_prefix="/api/v1/auth")


# user signup endpoint
@auth.post('/signup')
def signup():
    # retrieve payloads from request body
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    # validate the payloads
    if len(password) < 6:
        return jsonify({
            'error': "Password too short"
        }), HTTP_400_BAD_REQUEST

    if len(username) < 3:
        return jsonify({
            'error': "Username too short"
        }), HTTP_400_BAD_REQUEST

    if not username.isalnum() or " " in username:
        return jsonify({
            'error': "Username should be alphanumeric and no spaces"
        }), HTTP_400_BAD_REQUEST

    if not validators.email(email):
        return jsonify({
            'error': "Email is not valid"
        }), HTTP_400_BAD_REQUEST

    # check if the user exist in the db
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({
            'error': "Email already taken"
        }), HTTP_409_CONFLICT

    if User.query.filter_by(username=username).first() is not None:
        return jsonify({
            'error': "Username already taken"
        }), HTTP_409_CONFLICT

    # hash/encrypt the password string
    password_hash = generate_password_hash(password)

    # instantiate a new user object
    new_user = User(
        username=username,
        email=email,
        password=password_hash
    )

    # commit/save the new user to the db
    db.session.add(new_user)
    db.session.commit()

    # send api response
    return jsonify({
        'message': "Signed Up Successfully",
        'user': {
            'username': username,
            'email': email
        }
    }), HTTP_201_CREATED


# user login endpoint
@auth.post('/login')
def login():
    return jsonify({
        'message': "User logged in successfully"
    })
