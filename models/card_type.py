from main import db

class CardType(db.Model):
    __tablename__ = "CardType"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    card = db.relationship("Card", backref="card_type", lazy=True)

    def __init__(self, name):
        self.name = name

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
