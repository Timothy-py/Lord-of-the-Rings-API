from flask import Blueprint, jsonify


# configure characters route
characters = Blueprint('characters', __name__, url_prefix='/api/v1/characters')


# endpoint to retrieve all characters
@characters.get('/')
def get_all_characters():
    return jsonify({
        'message': []
    })


# return all quotes from a particular character(id)
@characters.get('/<int:id>/quotes')
def get_character_quotes(id):
    return jsonify({
        'message': []
    })


# endpoint for a user to favorite a specific character(id)
@characters.post('/<int:id>/favorites')
def favorite_character(id):
    return jsonify({
        'message': 'Character added to favorite successfully'
    })


# endpoint for a user to favorite a quote(id) with its character(id) info
@characters.post('/<int:quote_id>/quotes/<int:character_id>/favorites')
def favorite_quote_and_character(quote_id, character_id):
    return jsonify({
        'message': 'Quote added to favorites successfully'
    })


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
