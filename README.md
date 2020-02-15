Azramind is a command-line game modeled after the popular board game Mastermind. It is written in Python/Flask with a Postgres database. The game-play repository can be found here: [Link to Azramind Game Play](https://github.com/azra-mind/game-azramind)

- [Project URL](https://github.com/azra-mind)
- [Game Play Repo](https://github.com/azra-mind/game-azramind)
- [Link to Deployed API](https://azramind.herokuapp.com/)

# API Documentation

## Endpoints

### User Routes

| Method | Endpoint | Description                    |
| ------ | -------- | ------------------------------ |
| POST   | `/user`  | enables adding a new user      |
| GET    | `/user`  | returns new a user by username |
| GET    | `/users` | fetches list of all users      |

### Score Routes

| Method | Endpoint            | Description                                          |
| ------ | ------------------- | ---------------------------------------------------- |
| POST   | `/score`            | takes user_id, difficulty, num_tries. Adds new score |
| GET    | `/<username>/score` | fetches all scores for the specified username        |
| GET    | `/scores`           | fetches list of all users scores                     |

## Data Model

### `users` table

```
{
        id: INT ,
        username: STRING (80 CHAR) ,
        password: STRING (80 CHAR)
}
```

### `scores` table

```
{
        id: INT ,
        date_time: DATETIME ,
        user_id: FOREIGN KEY (users.id),
        difficulty: INT,
        num_tries: INT
    }
```

## CODE STRUCTURE:

### app.py

- contains the the flask app, app configurations, and resource end-points

### models directory

- `user.py` has the user model
- `score.py` has the score model that keeps track of game scores.

### resources directory

- `user.py` contains the api resources that pair with the `user model`
- `score.py` contains the api resources that pair with the `score model`

## HOW I APPROACHED BUILDING THIS GAME:

I built this game in Python because it is my favorite language to code in out of the ones I've tried thus far (Ruby, Javascript, Python). In addition, I really enjoy building APIs and thought this would be a great way for me to learn how to do so using Python.

While I knew how to bulid APIs in Node.js, and knew enough Python to solve CS coding challenge style problems in Algorithms, Datastructures, I had never built a backend utilizing Object Oriented Programming, nor had I ever built a REST API from scratch using a Python framework such as Flask or Django prior to building this project. I decided to use this challenge as a forcing function to teach myself something that I'd been meaning to learn anyway: How to build a backend and RESTful API in Flask. I chose Flask over Django because it is a more light-weight framework that I could learn and deploy quickly, yet it scales well since companies like Netflix, Reddit, an Lyft use it.

I spent the first day understanding and fulfilling the basic requirements for the project. Then, I spent about 3 days learning how to build a backend in Flask. I spent another 3 days building out the backend as well as a proper game program with a user menu etc. I spent the final day writing documentation and QA testing the project.

### WHAT'S NEXT:

I plan to continue working on this project to build upon my knowledge.

#### Game Play Interface

- Add the ability for the player to configure difficult levels
- Build out a frontend in React.js

#### Backend

- Add unit tests to the backend repo
- Add user authorization (login/password)
- Add a lookup table for difficulty levels (easy/medium/hard)
