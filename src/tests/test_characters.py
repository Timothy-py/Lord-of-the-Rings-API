import unittest
from .. import create_app
from ..config.config import config_dict
from ..model import db
from flask_jwt_extended import create_access_token


class CharactersTestCase(unittest.TestCase):

    def setUp(self):
        """
        setup test environment
        """

        # load an instance of app with testing configurations
        self.app = create_app(config=config_dict['testing'])

        # create app context
        self.appctx = self.app.app_context()

        # push the app context
        self.appctx.push()

        # create a test client
        self.client = self.app.test_client()

        # create the database
        db.create_all()

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def tearDown(self):
        """
        destroy the test environment
        """
        # destroy the database
        db.drop_all()

        # remove the app context
        self.appctx.pop()

        self.app = None
        self.client = None

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def test_get_all_characters(self):

        response = self.client.get('/api/v1/characters/?limit=2')

        assert response.status_code == 200

        assert len(response.json['characters']['docs']) != 3

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def test_get_character_quotes(self):

        response = self.client.get(
            '/api/v1/characters/5cd99d4bde30eff6ebccfbbf/quotes')

        assert response.status_code == 200

        assert response.json['message'] == "Quotes retrieved successfully"

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def test_favorite_character(self):

        access_token = create_access_token(identity=1)
        headers = {
            "Authorization": "Bearer %s" % access_token
        }

        response = self.client.post(
            '/api/v1/characters/5cd99d4bde30eff6ebccfbbf/favorites', headers=headers)

        assert response.status_code == 201

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def test_favorite_quote_and_character(self):

        access_token = create_access_token(identity=1)
        headers = {
            "Authorization": "Bearer %s" % access_token
        }

        response = self.client.post(
            '/api/v1/characters/5cd99d4bde30eff6ebccfe9e/quotes/5cd96e05de30eff6ebcce7ea/favorites', headers=headers)

        assert response.status_code == 201
