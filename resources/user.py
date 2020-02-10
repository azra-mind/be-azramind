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

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": f"username {data['username']} created successfully."}, 201

    # GET /username
    def get(self, username):
        try:
            user = UserModel.find_by_name(username)
        except:
            return {"message": "An error occurred searching for that username"}, 500

        if user:
            return user.json_username()
        return {'message': 'username not found'}, 404


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
