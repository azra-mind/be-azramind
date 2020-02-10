from db import db


class ScoreModel(db.Model):
    __tablename__ = 'scores'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    difficulty = db.Column(db.Integer)
    num_tries = db.Column(db.Integer)

    # sees that we have store_id, below essentiall adds a reference
    store = db.relationship('ScoreModel')

    def __init__(self, user_id, difficulty, num_tries):
        self.user_id = user_id
        self.difficulty = difficulty
        self.num_tries = num_tries

    def json(self):
        # need the .all() when lazy=dynamic turns self.items into query builder
        return {'id': self.id,
                'user_id': self.user_id,
                'difficulty': self.difficulty,
                'num_tries': self.num_tries
                }

    @classmethod
    def find_scores_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id)

    @classmethod
    def find_by_username(cls, username):
        pass

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


class ScoreList(Resource):
    def get(self):

        try:
            users = {'scores': [score.json()
                                for score in ScoreModel.query.all()]}
        except:
            return {"message": "An error occurred finding the score list"}, 500
        if users:
            return users
        return {'message': 'Score List not found'}, 404
