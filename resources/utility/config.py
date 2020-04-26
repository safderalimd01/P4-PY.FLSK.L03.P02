from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor
import pymysql

import os
from flask import Flask, request

app = Flask(__name__)

def db_connect():
    mysql = MySQL(cursorclass=DictCursor)
    app.config['MYSQL_DATABASE_HOST'] = os.environ.get('host')
    app.config['MYSQL_DATABASE_DB'] = os.environ.get('database')
    app.config['MYSQL_DATABASE_USER'] = os.environ.get('user')
    app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('password')
    mysql.init_app(app)
    return mysql
