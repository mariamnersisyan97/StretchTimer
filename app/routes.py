# Flask useful routes functions
import time
from flask import flash, render_template, redirect, url_for, abort, Blueprint, Response, request, jsonify
# For random user image
from flask_gravatar import Gravatar
# Managing logged in Users status
from flask_login import login_user, login_required, current_user, logout_user
# Password Security
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.security import generate_password_hash, check_password_hash
# FORMS
from app.forms import RegisterForm, LoginForm
# Database Tables Managing with SQLAlchemy
from app.tables import User, db
# Decorators
from app.decorators import admin_only

# gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False,
#                     use_ssl=False,
#                     base_url=None)

app_index = Blueprint('index_route', __name__,
                      template_folder='templates')
app_accounts = Blueprint('accounts_route', __name__,
                         template_folder='templates/accounts')


# Index Route
@app_index.route('/')
def home():
    return render_template('index.html')


@app_index.route('/about')
def about():
    return render_template('about.html')


@app_accounts.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        email = form.email.data
        if User.query.filter_by(email=email).first():
            flash("Email already exists. Try to log in.")
            return redirect(url_for("accounts_route.login"))
        password = generate_password_hash(form.password.data, salt_length=8)
        name = form.name.data
        new_user = User(email=email, password=password, name=name)
        db.session.add(new_user)
        db.session.commit()
        login_user(User.query.filter_by(email=email).first())
        return redirect(url_for("home"))
    return render_template("register.html", form=form)


@app_accounts.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()
        if not user:
            flash("Unknown Email, Try Again.")
            return render_template("login.html", form=form)
        password = form.password.data
        if not check_password_hash(user.password, password):
            flash("Wrong Password, Try Again.")
            return render_template("login.html", form=form)
        login_user(user)
        return redirect(url_for("index_route.home"))
    return render_template("login.html", form=form)


@app_accounts.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index_route.home'))
