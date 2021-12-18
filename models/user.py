from main import db
from sqlalchemy.sql import func
from werkzeug.security import check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    date_created = db.Column(db.DateTime(), server_default=func.now())
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    user_settings = db.relationship("UserSettings", backref="user", lazy=False, uselist=False)

    decks = db.relationship("Deck", backref="user", lazy="joined")

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    @property
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

    def check_password(self, password):
        return check_password_hash(self.password, password)
