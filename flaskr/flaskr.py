# all the imports
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from pprint import pprint

#CREATING THE FLASK INSTANCE
app = Flask(__name__)
app.config.from_object(__name__)

#load config from this file
app.config.update( dict(
		DATABASE = os.path.join(app.root_path, "flaskr.db") ,
		SECRET_KEY='development key',
    	USERNAME='admin',
    	PASSWORD='default'
	))

#overriding config from environment variable
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row

	return rv

@app.route('/')
def index() :
	rv = connect_db()
	return "hi"