from main import ma
from models.deck import Deck
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length

class DeckSchema(ma.SQLAlchemyAutoSchema):
    id = auto_field(dump_only=True)
    name = auto_field(required=True, validate=Length(min=1))

    class Meta:
        model = Deck
        load_instance = True

deck_schema = DeckSchema()
multi_deck_schema = DeckSchema(many=True)