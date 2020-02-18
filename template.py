from flask import Flask, request, render_template
from app import app
from models.score import ScoreModel


@app.route('/template/<username>')
def get_scores(username):
    try:
        scores = [score.json()
                  for score in ScoreModel.find_scores_by_username(username)]
    except:
        return {"message": "An error occurred searching for that user_id"}, 500

    return render_template('index.html', scores=scores)

    return {'message': 'scores not found'}, 404


if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        # creates the db upon the first request
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
