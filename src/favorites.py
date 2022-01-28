from flask import Blueprint, jsonify


# configure favorites base route
favorites = Blueprint('favorites', __name__, url_prefix='/api/v1/favorites')


# retrieve all favorites of the logged in user
@favorites.get('/')
def get_all_favorites():
    return jsonify({
        'message': "ALl favorites retrieved successfully"
    })
