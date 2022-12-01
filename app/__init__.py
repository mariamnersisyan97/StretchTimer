from run import db
import os
import json
from flask import Flask
from flask import request


def create_app(config_name):
    app = Flask(__name__)
    # app.config.from_object(os.environ['APP_SETTINGS'])
    db.init_app(app)
    app.register_blueprint(test)
