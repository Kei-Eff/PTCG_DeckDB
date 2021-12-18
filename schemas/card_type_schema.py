from main import ma
from models.card_type import CardType
from marshmallow_sqlalchemy import auto_field
from marshmallow.validate import Length

class CardTypeSchema(ma.SQLAlchemyAutoSchema):
    id = auto_field(dump_only=True)
    name = auto_field(required=True, validate=Length(min=1))
    # card = ma.Nested("CardSchema")

    class Meta:
        model = CardType
        load_instance = True

card_type_schema = CardTypeSchema()
card_types_schema = CardTypeSchema(many=True)
