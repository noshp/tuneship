from os.path import join, isfile

from flask import Flask, render_template, make_response, jsonify

#Config

app = Flask(__name__, instance_relative_config=True)

if isfile(join('instance', 'flask_full.cfg')):
    app.config.from_pyfile('flask_full.cfg')
else:
    app.config.from_pyfile('flask.cfg')

#Load the views
from . import views
