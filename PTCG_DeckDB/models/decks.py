from main import db

ownerships = db.Table(
    'ownerships',
    db.Column('user_id', db.Integer, db.ForeignKey('flasklogin-users.id'), primary_key=True),
    db.Column('deck_id', db.Integer, db.ForeignKey('deck.deck_id'), primary_key=True)
)


class Deck(db.Model):
    __tablename__ = "decks"
    deck_id = db.Column(db.Integer, primary_key=True)
    deck_name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), default="No Description Provided")
    cost = db.Column(db.Integer, nullable=False, server_default="0")

    creator_id = db.Column(db.Integer, db.ForeignKey('flasklogin-users.id'))

    def __init__(self, deck_name):
        self.deck_name = deck_name

    owners = db.relationship(
        'User',
        secondary=ownerships,
        backref=db.backref('owned_decks')
    )