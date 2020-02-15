from flask_restful import Resource, reqparse
from models.score import ScoreModel
from models.user import UserModel


class Score(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('user_id',
                        type=int,
                        required=True,
                        help="user_id cannot be left blank!"
                        )
    parser.add_argument('difficulty',
                        type=int,
                        required=True,
                        help="difficulty level cannot be left blank!"
                        )
    parser.add_argument('num_tries',
                        type=int,
                        required=True,
                        help="num_tries cannot be left blank!"
                        )

# POST /score
    @classmethod
    def post(cls):
        data = cls.parser.parse_args()

        score = ScoreModel(
            data['user_id'], data['difficulty'], data['num_tries'])

        try:
            score.save_to_db()
        except:
            return {"message": "An error occurred inserting the score"}, 500

        return score.json(), 201


class UserScores(Resource):

    # GET /<username>/score
    def get(self, username):
        try:

            scores = {'scores': [
                score.json() for score in ScoreModel.find_scores_by_username(username)]}

        except:
            return {"message": "An error occurred searching for that user_id"}, 500

        if len(scores['scores']) > 0:
            return scores, 200

        return {'message': 'scores not found'}, 404


class ScoreList(Resource):
    # GET all /scores
    def get(self):
        try:
            scores = {'scores': [score.json()
                                 for score in ScoreModel.query.all()]}
        except:
            return {"message": "An error occurred finding the score list"}, 500
        if scores:
            return scores
        return {'message': 'Score List not found'}, 404
