"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7iqd269vf5qb7grjg-a.oregon-postgres.render.com",
        database="todo_t9mj",
        user="todo_t9mj_user",
        password="yLovqCBB2WMSo61RPZ5Mn3sLPufJsW6S")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
