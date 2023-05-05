"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaainik728r886m37ng-a.oregon-postgres.render.com",
        database="todo_6cgg",
        user="todo_6cgg_user",
        password="pQenwxp7tThJQIHpbiUHDvuWneTDPQPm")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
