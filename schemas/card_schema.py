from main import ma
from models.card import Card
from marshmallow_sqlalchemy import auto_field
from marshmallow import validate
from schemas.card_type_schema import CardTypeSchema

class CardSchema(ma.SQLAlchemyAutoSchema):
    id = auto_field(dump_only=True)
    name = auto_field(required=True, validate=validate.Length(min=1))
    set = auto_field(required=True, validate=validate.Length(min=1))
    quantity= auto_field(required=True, validate=validate.Range(min=1))
    cost = auto_field(validate=validate.Range(min=0.00))
    deck = ma.Nested("DeckSchema", exclude=("cards",))
    card_type = ma.Nested("CardTypeSchema")

    class Meta:
        model = Card
        load_instance = True

card_schema = CardSchema()
cards_schema = CardSchema(many=True)
card_update_schema = CardSchema(partial=True)