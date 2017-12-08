from os.path import join, isfile
from flask import Flask, render_template, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_migrate import Migrate
#Config

application = Flask(__name__, instance_relative_config=True)

if isfile(join('instance', 'flask_full.cfg')):
    application.config.from_pyfile('flask_full.cfg')
else:
    application.config.from_pyfile('flask.cfg')

db = SQLAlchemy(application)
migrate = Migrate(application,db)
from tuneship import views
from tuneship.models import *

#Create the Flask-Restless API Manager
manager = APIManager(application, flask_sqlalchemy_db=db)

manager.create_api(Data, methods=['GET'])
manager.create_api(TunesData, methods=['GET', 'POST'])