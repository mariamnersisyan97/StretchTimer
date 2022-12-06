from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, URL, Email, email_validator
from flask_ckeditor import CKEditorField


class RegisterForm(FlaskForm):
    email = StringField("Email", render_kw={"placeholder": "Email"}, validators=[DataRequired(), Email()])
    password = PasswordField("Password", render_kw={"placeholder": "Password"}, validators=[DataRequired()])
    name = StringField("Name", render_kw={"placeholder": "Full Name"}, validators=[DataRequired()])
    submit = SubmitField("Create Account")


class LoginForm(FlaskForm):
    email = StringField("Email", render_kw={"placeholder": "Email"}, validators=[DataRequired(), Email()])
    password = PasswordField("Password", render_kw={"placeholder": "Password", "cols": "5"}, validators=[
        DataRequired()])
    submit = SubmitField("Create Account")


class ChangeEmailForm(FlaskForm):
    password = PasswordField("Current Password", validators=[DataRequired()])
    email = StringField("Edit Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Change Email")


class ChangePasswordForm(FlaskForm):
    current_password = PasswordField("Current Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", validators=[DataRequired()])
    submit = SubmitField("Change Password")
