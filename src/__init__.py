import os
from flask import Flask

DATABASE_URL_PROJECT = os.getenv('DATABASE_URL_PROJECT', 'sqlite:///project.db') if os.environ.get(
    'DATABASE_URL_PROJECT') != 'default' else 'sqlite:///project.db'


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL_PROJECT
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'frase-secreta'
    app.config['PROPAGATE_EXCEPTIONS'] = True

    return app
