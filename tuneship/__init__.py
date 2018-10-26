from os.path import join, isfile
from flask import Flask, render_template, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restless import APIManager
from flask_migrate import Migrate
from . import Config
import os
#Config

application = Flask(__name__)

if os.getenv('APP_ENV') == 'DEVELOPMENT':
    application.config.from_object(Config.DevelopmentConfig)
elif os.getenv('APP_ENV') == 'PRODUCTION':
    application.config.from_object(Config.ProductionConfig)

db = SQLAlchemy(application)
migrate = Migrate(application,db)

from tuneship import views
from tuneship.models import *

#Create the Flask-Restless API Manager
manager = APIManager(application, flask_sqlalchemy_db=db)

manager.create_api(Data, methods=['GET'])
manager.create_api(TunesData, methods=['GET', 'POST'])