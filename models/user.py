import sqlite3
from db import db

# each model will be an extension of db.Model class


class UserModel(db.Model):

    # tell SQLAlchemy where the model will be stored
    __tablename__ = 'users'

    # define the schema for the users table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    # initializing user class
    def __init__(self, username, password="Superpass01!"):
        self.username = username
        self.password = password

    # adding a user to the db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    def json_username(self):
        return {'id': self.id, 'username': self.username}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
