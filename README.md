# tuneship
Webapp to display outgoing slack channel webhooks including links.

## Setup dev environment
---
Use `pipenv`

```shell
#install dependencies and virtualenv
pipenv install --python 3.7

#Then activate your virtual env
pipenv shell
```
## Running application

Once the postgres database is up and running and all requirements are installed.
Export the Flask app in your terminal session.

```shell
export FLASK_APP=application.py
```

Then run the flask app

```shell
flask run
```

## Updating db and migrations
---
**Have a postgres instance running on port 5432**

Supplied is a `docker-compose.yml` if you want to run a postgres container.

```shell
docker-compose up
```

We are using Flask-Migrate to handle all the database migrations.
For initial db setup:

```shell
flask db init

```
To migrate follow these steps:

```shell
flask db migrate

#then to apply the migrations
flask db upgrade

```




