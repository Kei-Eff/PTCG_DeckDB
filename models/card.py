from main import db
from sqlalchemy.sql import func

class Card(db.Model):
    __tablename__ = "Card"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime(), server_default=func.now())
    set = db.Column(db.String(80), nullable=False)
    card_type_id = db.Column(db.Integer, db.ForeignKey("CardType.id"), nullable=False)
    quantity = db.Column(db.Integer, default=1)
    deck_id = db.Column(db.Integer, db.ForeignKey("Deck.id"), nullable=False)

    def __init__(self, name, set, quantity):
        self.name = name
        self.set = set
        self.quantity = quantity

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "set": self.set,
            "quantity": self.quantity
        }
