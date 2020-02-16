import os
from flask import Flask
from flask_restful import Api, Resource
from resources.user import User, UserList
from resources.score import Score, ScoreList, UserScores
# make sure you import all resources for tables you want built:
from datetime import timedelta


# initiating the flask app
app = Flask(__name__)

# configs:
# shows more error messages
app.config['PROPAGATE_EXCEPTIONS'] = True

# for development purposes debug = True, set to false in production
app.config['DEBUG'] = os.environ.get(
    'DEBUG', True)

# SQL alchemy config, connection to the DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', "sqlite:///data.db")

# sqlalchemy event notfication system. Don't need it here, set to False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# build the basic api
api = Api(app)


class Hello(Resource):
    def get(self):
        return 'Hello World! Is this API up?'


api.add_resource(Hello, '/')
api.add_resource(User, '/user')
api.add_resource(UserList, '/users')
api.add_resource(Score, '/score')
api.add_resource(UserScores, '/<username>/scores')
api.add_resource(ScoreList, '/scores')


if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        # creates the db upon the first request
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
