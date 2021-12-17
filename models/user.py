from main import db
from werkzeug.security import check_password_hash
from sqlalchemy.sql import func

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    date_created = db.Column(db.DateTime(), server_default=func.now())
    email_address = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    user_settings = db.relationship('UserSettings', backref='user', lazy=False, uselist=False)

    def __init__(self, username, password, email_address):
        self.username = username
        self.password = password
        self.email_address = email_address

    @property
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email_address": self.email_address
        }
