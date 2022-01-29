from flask import Blueprint, jsonify, request
import requests
import os
from flask_jwt_extended import get_jwt_identity, jwt_required
from src.model import Favorite, db

from src.constants.http_status_codes import HTTP_500_INTERNAL_SERVER_ERROR, HTTP_200_OK, HTTP_201_CREATED


# configure characters route
characters = Blueprint('characters', __name__, url_prefix='/api/v1/characters')

# load api api_key
api_key = os.environ.get("API_KEY")


# endpoint to retrieve all characters
@characters.get('/')
def get_all_characters():

    # declare pagination parameters
    limit = request.args.get('limit', 100, type=int)
    page = request.args.get('page', 1, type=int)
    offset = request.args.get('offset', '', type=int)

    # make request to the API
    response = requests.get(
        url="https://the-one-api.dev/v2/character",
        params={
            "limit": limit,
            "page": page,
            "offset": offset
        },
        headers={
            "Authorization": 'Bearer %s' % api_key
        }
    )

    if response.status_code != 200:
        return jsonify({
            'message': response.response
        }), HTTP_500_INTERNAL_SERVER_ERROR

    return jsonify({
        'message': 'Characters retrieved successfully',
        'characters': response.json()
    }), HTTP_200_OK


# return all quotes from a particular character(id)
@characters.get('/<string:id>/quotes')
def get_character_quotes(id):

    # declare pagination parameters
    limit = request.args.get('limit', 100, type=int)
    page = request.args.get('page', 1, type=int)
    offset = request.args.get('offset', '', type=int)

    # make request to the API
    response = requests.get(
        url="https://the-one-api.dev/v2/character/%s/quote" % id,
        params={
            "limit": limit,
            "page": page,
            "offset": offset
        },
        headers={
            "Authorization": 'Bearer %s' % api_key
        }
    )

    if response.status_code != 200:
        return jsonify({
            'message': response.response
        }), HTTP_500_INTERNAL_SERVER_ERROR

    return jsonify({
        'message': 'Quotes retrieved successfully',
        'quotes': response.json()
    }), HTTP_200_OK


# endpoint for a user to favorite a specific character(id)
@characters.post('/<string:id>/favorites')
@jwt_required()
def favorite_character(id):

    # get logged in user id
    logged_in_user_id = get_jwt_identity()

    # make request to the API
    response = requests.get(
        url="https://the-one-api.dev/v2/character/%s/" % id,
        headers={
            "Authorization": 'Bearer %s' % api_key
        }
    )

    if response.status_code != 200:
        return jsonify({
            'message': response.reason
        }), HTTP_500_INTERNAL_SERVER_ERROR

    # get character data
    character = response.json()['docs'][0]

    # instantiate a new favorite object
    favorite = Favorite(
        height=character['height'],
        race=character['race'],
        gender=character['gender'],
        birth=character['birth'],
        spouse=character['spouse'],
        death=character['death'],
        realm=character['realm'],
        hair=character['hair'],
        name=character['name'],
        wikiUrl=character['wikiUrl'],
        user_id=logged_in_user_id
    )

    # save to database
    db.session.add(favorite)
    db.session.commit()

    return jsonify({
        "message": "Character saved as favorite",
        "favorite": {
            'id': favorite.id,
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
        }
    }), HTTP_201_CREATED


# endpoint for a user to favorite a quote(id) with its character(id) info
@characters.post('/<string:character_id>/quotes/<string:quote_id>/favorites')
@jwt_required()
def favorite_quote_and_character(quote_id, character_id):

    # get logged in user id
    logged_in_user_id = get_jwt_identity()

    # make request to the API to get Quote
    res_quote = requests.get(
        url="https://the-one-api.dev/v2/quote/%s/" % quote_id,
        headers={
            "Authorization": 'Bearer %s' % api_key
        }
    )

    res_character = requests.get(
        url="https://the-one-api.dev/v2/character/%s/" % character_id,
        headers={
            "Authorization": 'Bearer %s' % api_key
        }
    )

    if res_quote.status_code != 200 or res_character.status_code != 200:
        return jsonify({
            'message': 'Server encountered problem'
        }), HTTP_500_INTERNAL_SERVER_ERROR

    # get quote data
    quote = res_quote.json()['docs'][0]

    # get character data
    character = res_character.json()['docs'][0]

    # instantiate a new favorite object
    favorite = Favorite(
        dialog=quote['dialog'],
        movie=quote['movie'],
        height=character['height'],
        race=character['race'],
        gender=character['gender'],
        birth=character['birth'],
        spouse=character['spouse'],
        death=character['death'],
        realm=character['realm'],
        hair=character['hair'],
        name=character['name'],
        wikiUrl=character['wikiUrl'],
        user_id=logged_in_user_id
    )

    # save to database
    db.session.add(favorite)
    db.session.commit()

    return jsonify({
        "message": "Quote saved as favorite",
        "favorite": {
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
        }
    }), HTTP_201_CREATED

# {
#     "_id": "5cd99d4bde30eff6ebccfbd4",
#     "height": "",
#     "race": "Human",
#     "gender": "Male",
#     "birth": "FA 440",
#     "spouse": "Unnamed wife",
#     "death": "FA 489",
#     "realm": "",
#     "hair": "",
#     "name": "Andróg",
#     "wikiUrl": "http://lotr.wikia.com//wiki/Andr%C3%B3g"
# }


#  {
#     "_id": "5cd96e05de30eff6ebcce7e9",
#     "dialog": "Deagol!",
#     "movie": "5cd95395de30eff6ebccde5d",
#     "character": "5cd99d4bde30eff6ebccfe9e"
# },
