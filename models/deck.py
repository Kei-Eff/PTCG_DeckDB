from main import db
from sqlalchemy.sql import func

class Deck(db.Model):
    __tablename__ = "Deck"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime(), server_default=func.now())
    # user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    # card = db.relationship('Card', backref='deck', lazy=True)

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
