import unittest
from .. import create_app
from ..config.config import config_dict
from ..model import db, User
from werkzeug.security import generate_password_hash


class AuthTestCase(unittest.TestCase):

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
    def test_user_signup(self):
        data = {
            "username": "testuser",
            "email": "testuser@gmail.com",
            "password": generate_password_hash("testuser123")
        }
        response = self.client.post('/api/v1/auth/signup', json=data)

        user = User.query.filter_by(email="testuser@gmail.com").first()

        assert user.username == data['username']

        assert response.status_code == 201

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def test_user_login(self):
        data = {
            "email": "user@gmail.com",
            "password": "testuser123"
        }

        response = self.client.post('/api/v1/auth/login', json=data)

        assert response.status_code == 401

    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
