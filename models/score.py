from db import db
from resources.user import UserModel
from datetime import datetime


class ScoreModel(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    date_time = db.Column(db.DateTime, default=datetime.now)
    # stores # of digits player had to guess
    difficulty = db.Column(db.Integer)
    num_tries = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # sees that we have user_id as foreign key, below adds a reference to users table via the model
    user = db.relationship('UserModel')

    def __init__(self, user_id, difficulty, num_tries):
        self.user_id = user_id
        self.difficulty = difficulty
        self.num_tries = num_tries

    def json(self):
        return {'id': self.id,
                'date_time': str(self.date_time)[:19],
                'user_id': self.user_id,
                'difficulty': self.difficulty,
                'num_tries': self.num_tries
                }

    @classmethod
    def find_scores_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id)

    @classmethod
    # need the .all() when doing join cuz of lazy='dynamic' allows for more flexible querying
    def find_scores_by_username(cls, username):
        return cls.query.join(UserModel).filter_by(username=username).all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
