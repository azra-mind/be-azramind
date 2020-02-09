from flask import Flask
from flask_restful import Resource, Api, reqparse


# initiating the flask app
app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        return 'Hello World! Is this API up?'


api.add_resource(Hello, '/')
app.run(port=5000, debug=True)
