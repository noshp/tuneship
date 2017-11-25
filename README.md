#tuneship
Webapp to display outgoing slack channel webhooks including links.

## Setup dev environment
---
Run `virtualenv`

```shell
virtualenv venv -p python3

#Then activate your virtual env
source venv/bin/activate

#Install requirements
pip install -r requirements.txt
```

**Have a postgres instance running on port 5432**

**Create the db**

```shell
python db_create.py
```

## Running application

Once the postgres database is up and running and all requirements are installed.
Export the Flask app in your terminal session.

```shell
export FLASK_APP=run.py
```

Then run the flask app

```shell
flask run
```


