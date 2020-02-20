import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

# this is the equivalent of the data-model file in node.js

# it's a resource


class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=False
                        )

    # POST to /register
    @classmethod
    def post(cls):
        data = cls.parser.parse_args()
        user_existing = UserModel.find_by_username(data['username'])

        if user_existing:
            return {"message": f"A user with {data['username']} already exists"}, 400
            # return user_existing.json_username(), 201

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return user.json_username(), 201

    # GET /user
    @classmethod
    def get(cls):
        data = cls.parser.parse_args()
        username = data['username']

        try:
            user = UserModel.find_by_username(username)
        except:
            return {"message": f"An error occurred searching for the username {username}"}, 500

        if user:
            return user.json_username()
        return {'message': f'username {username} not found'}, 404


# get a list of all users
class UserList(Resource):
    def get(self):

        try:
            users = {'users': [user.json_username()
                               for user in UserModel.query.all()]}
        except:
            return {"message": "An error occurred finding the user list"}, 500
        if users:
            return users
        return {'message': 'ItemList not found'}, 404
