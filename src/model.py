from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# instantiate SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.Text(), nullable=False)
    favorites = db.relationship('Favorite', backref='user')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())

    def __repr__(self) -> str:
        return "User>>> {self.username}"


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dialog = db.Column(db.String(50))
    movie = db.Column(db.String(50))
    height = db.Column(db.String(50))
    race = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    birth = db.Column(db.String(50))
    spouse = db.Column(db.String(50))
    death = db.Column(db.String(50))
    realm = db.Column(db.String(50))
    hair = db.Column(db.String(50))
    name = db.Column(db.String(50))
    wikiUrl = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self) -> str:
        return "Favorite by User id-{self.user_id}"
