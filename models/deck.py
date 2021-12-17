from main import db
from sqlalchemy.sql import func

class Deck(db.Model):
    __tablename__ = "deck"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    date_created = db.Column(db.DateTime(), server_default=func.now())

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
        