from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from run import db
from sqlalchemy.orm import relationship


# CONNECT TO DB


# CONFIGURE TABLES
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    img_url = db.Column(db.String(250), nullable=True)
    # many_to_user_relation = relationship("TABLE_CLASS_NAME", back_populates="user")


# CREATE ALL TABLES
with app_bp.app_context():
    db.create_all()
