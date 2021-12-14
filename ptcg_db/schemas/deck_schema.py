from main import ma
from models.decks import Deck
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length, Range

class DeckSchema(ma.SQLAlchemyAutoSchema):
    deck_id = auto_field(dump_only=True)
    deck_name = auto_field(required=True, validate=Length(min=1))
    description = auto_field(validate=Length(min=1))
    cost = auto_field(required=False, validate=Range(0, 500))
    creator = ma.Nested(
        "UserSchema",
        only=("id", "name", "email",)
        )
    owners = ma.Nested(
        "UserSchema",
        only=("id", "name", "email",)
    )

    class Meta:
        model = Deck
        load_instance = True

deck_schema = DeckSchema()
decks_schema = DeckSchema(many=True)