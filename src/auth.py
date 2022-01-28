from flask import Blueprint, jsonify


# configure authentication route
auth = Blueprint('auth', __name__, url_prefix="/api/v1/auth")


# user signup endpoint
@auth.post('/signup')
def register():
    return jsonify({
        'message': "User registered successfully"
    })


# user login endpoint
@auth.post('/login')
def login():
    return jsonify({
        'message': "User logged in successfully"
    })
