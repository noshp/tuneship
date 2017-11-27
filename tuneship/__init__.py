from os.path import join, isfile
from flask import Flask, render_template, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_migrate import Migrate
#Config

app = Flask(__name__, instance_relative_config=True)

if isfile(join('instance', 'flask_full.cfg')):
    app.config.from_pyfile('flask_full.cfg')
else:
    app.config.from_pyfile('flask.cfg')

db = SQLAlchemy(app)
migrate = Migrate(app,db)
from tuneship import views
from tuneship.models import *

#Create the Flask-Restless API Manager
manager = APIManager(app, flask_sqlalchemy_db=db)

manager.create_api(Data, methods=['GET'])