from main import ma
from models.deck import Deck
from marshmallow_sqlalchemy import auto_field
from marshmallow import validate

class DeckSchema(ma.SQLAlchemyAutoSchema):
    id = auto_field(dump_only=True)
    name = auto_field(required=True, validate=validate.Length(min=1))
    user = ma.Nested("UserSchema")
    cards = ma.Nested("CardSchema")

    class Meta:
        model = Deck
        load_instance = True

deck_schema = DeckSchema()
decks_schema = DeckSchema(many=True)
deck_update_schema = DeckSchema(partial=True)
