from flask import Flask, Blueprint
from .extensions import mysql
from .admin import main
from .product import product


def create_app():
    app = Flask(__name__)

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'qwebnm123'
    app.config['MYSQL_DB'] = 'umbrellapos'
    mysql.init_app(app)

    app.register_blueprint(main)
    app.register_blueprint(product)

    return app
