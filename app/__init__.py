"""This is init module."""

from flask import Flask

import logging
from logging.handlers import RotatingFileHandler

from config import Config


def create_app():
    app = Flask(__name__)
    Config()
    setup_logging(app)
    register_blueprints(app)
    return app


def register_blueprints(app):
    from app.message.controller import message_thread
    from app.thread.controller import thread
    app.register_blueprint(thread, url_prefix='/thread')
    app.register_blueprint(message_thread, url_prefix='/thread')


def setup_logging(app):
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    knock_logging_handler = RotatingFileHandler(Config.LOG_FILENAME, maxBytes=10000000, backupCount=1)
    knock_logging_handler.setLevel(logging.DEBUG)
    knock_logging_handler.setFormatter(formatter)
    app.logger.addHandler(knock_logging_handler)
