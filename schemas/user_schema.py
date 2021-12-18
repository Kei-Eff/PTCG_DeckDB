from main import ma
from models.user import User
from marshmallow_sqlalchemy import auto_field
from marshmallow import fields, exceptions, validate
from werkzeug.security import generate_password_hash

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    id = auto_field(dump_only=True)
    username = auto_field(required=True, validate=validate.Length(1))
    password = fields.Method(
        required=True,
        load_only=True,
        deserialize="load_password"
    )
    email = auto_field(required=True, validate=validate.Email())

    decks = ma.Nested(
        "DeckSchema",
        only=("id", "name")
    )

    def load_password(self, password):
        if len(password)>=8:
            return generate_password_hash(password, method="sha256")
        raise exceptions.ValidationError("Password must be at least 8 characters.")


user_schema = UserSchema()
users_schema = UserSchema(many=True)
user_update_schema = UserSchema(partial=True)