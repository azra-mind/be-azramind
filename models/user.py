from db import db
import random

# each model will be an extension of db.Model class


class UserModel(db.Model):

    # tell SQLAlchemy the tablename
    __tablename__ = 'users'

    # define the schema for the users table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    # establish relationship with the child model i.e. ScoreModel
    # lazy = dynamic returns the query object so it can be further sliced (.eg .all(), .first())
    scores = db.relationship('ScoreModel', lazy='dynamic')

    # initializing user class
    def __init__(self, username, password=f"Super{random.randrange(511, 11571)}"):
        self.username = username
        self.password = password

    # find user by id
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    # find user by id
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    # adding a user to the db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # json for a username
    def json_username(self):
        return {'id': self.id, 'username': self.username}

    # json for getting scores by user
    def json_scores(self):
        return {'username': self.username, 'scores': [score.json() for score in self.scores.all()]}
