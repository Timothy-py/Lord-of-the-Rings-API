from flask import Blueprint, jsonify, request
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.model import Favorite, db
from flasgger import swag_from

from src.constants.http_status_codes import HTTP_200_OK

# configure favorites base route
favorites = Blueprint('favorites', __name__, url_prefix='/api/v1/favorites')


# retrieve all favorites of the logged in user
@favorites.get('/')
@jwt_required()
@swag_from('./docs/favorites/get_all_favorites.yaml')
def get_all_favorites():

    # get logged in user id
    logged_in_user_id = get_jwt_identity()

    # declare pagination parameters
    page = request.args.get('page', 1, type=int)
    size = request.args.get('size', 5, type=int)

    # query database for favorites data
    favorites = Favorite.query.filter_by(
        user_id=logged_in_user_id
    ).paginate(page=page, per_page=size)

    data = []

    for favorite in favorites.items:
        data.append({
            'id': favorite.id,
            'dialog': favorite.dialog,
            'movie': favorite.movie,
            'height': favorite.height,
            'race': favorite.race,
            'gender': favorite.gender,
            'birth': favorite.birth,
            'spouse': favorite.spouse,
            'death': favorite.death,
            'realm': favorite.realm,
            'hair': favorite.hair,
            'name': favorite.name,
            'wikiUrl': favorite.wikiUrl,
            'user_id': favorite.user_id,
            'created_at': favorite.created_at
        })

    meta = {
        "page": favorites.page,
        "pages": favorites.pages,
        "total_count": favorites.total,
    }

    return jsonify({
        'data': data,
        'meta': meta,
        'message': 'All your favorites retrieved successfully'
    }), HTTP_200_OK
