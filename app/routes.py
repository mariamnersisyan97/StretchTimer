# from flask import flash, render_template, redirect, url_for, abort
# from flask_gravatar import Gravatar
# from flask_login import login_user, login_required, current_user, logout_user
#
# from werkzeug.security import generate_password_hash, check_password_hash
# from werkzeug.security import generate_password_hash, check_password_hash
#
# from app.forms import RegisterForm, LoginForm
# from app.tables import User, db
# from app.decorators import admin_only
# from run import login_manager, app
#
# gravatar = Gravatar(app, size=100, rating='g', default='retro', force_default=False, force_lower=False,
#                     use_ssl=False,
#                     base_url=None)
#
#
# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(user_id)
#
#
# with app.app_context():
#     db.create_all()
#
#
# @app.route('/')
# def home():
#     # return render_template("index.html")
#     return '<p>Hello</p>'
#
#
# @app.route('/register', methods=["GET", "POST"])
# def register():
#     form = RegisterForm()
#     if form.validate_on_submit():
#         email = form.email.data
#         if User.query.filter_by(email=email).first():
#             flash("Email already exists. Try to log in.")
#             return redirect(url_for("login"))
#         password = generate_password_hash(form.password.data, salt_length=8)
#         name = form.name.data
#         new_user = User(email=email, password=password, name=name)
#         db.session.add(new_user)
#         db.session.commit()
#         login_user(User.query.filter_by(email=email).first())
#         return redirect(url_for("get_all_posts"))
#     return render_template("register.html", form=form)
#
#
# @app.route('/login', methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         email = form.email.data
#         user = User.query.filter_by(email=email).first()
#         if not user:
#             flash("Unknown Email, Try Again.")
#             return render_template("login.html", form=form)
#         password = form.password.data
#         if not check_password_hash(user.password, password):
#             flash("Wrong Password, Try Again.")
#             return render_template("/app/templates/accounts/login.html", form=form)
#         login_user(user)
#         return redirect(url_for("get_all_posts"))
#     return render_template("login.html", form=form)
#
#
# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('get_all_posts'))
