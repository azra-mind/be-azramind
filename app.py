from flask import Flask
from flask_restful import Api, Resource
# from flask_jwt import JWT
from resources.user import User, UserList
from resources.score import Score, ScoreList, UserScores
# make sure you import all resources for tables you want built:
# from security import authenticate, identity
from datetime import timedelta
# from db import db


# initiating the flask app
app = Flask(__name__)

# configs:

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = True
# SQL alchemy config, connection to the DB
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# build the basic api
api = Api(app)


class Hello(Resource):
    def get(self):
        return 'Hello World! Is this API up?'


api.add_resource(Hello, '/')
api.add_resource(User, '/register')
api.add_resource(UserList, '/users')
api.add_resource(Score, '/score')
api.add_resource(UserScores, '/<username>/scores/')


if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        # creates the db upon the first request
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
