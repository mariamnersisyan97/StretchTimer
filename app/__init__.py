from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from app.tables import db, User
import os
from flask import Flask
from app.routes import app_index, app_accounts

# App Init
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stretch-timer.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
# Database Init
db.init_app(app)
# TODO: Hide app config in environment variable
# app.config.from_object(os.environ['APP_SETTINGS'])

# Debugger toolbar
app.debug = True
toolbar = DebugToolbarExtension(app)

# CK EDITOR for advanced text field form input  field
# ckeditor = CKEditor(app)
# Bootstrap html integration
Bootstrap(app)

# Following logged user status
login_manager = LoginManager()
login_manager.init_app(app)

# App routes blueprints
app.register_blueprint(app_index)
app.register_blueprint(app_accounts)

# Create all tables imported from app.tables
# TODO: Add Database Migration.
with app.app_context():
    db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
