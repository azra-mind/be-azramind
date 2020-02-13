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
