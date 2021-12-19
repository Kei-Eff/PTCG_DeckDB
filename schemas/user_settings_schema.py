from main import ma
from models.user_settings import UserSettings
from marshmallow_sqlalchemy import auto_field

class UserSettingsSchema(ma.SQLAlchemyAutoSchema):
    id = auto_field(dump_only=True)
    is_dark_mode = auto_field(default=False)
    is_anon_mode = auto_field(default=False)
    user = ma.Nested("UserSchema", exclude=("user_settings",))

    class Meta:
        model = UserSettings
        load_instance = True

user_settings_schema = UserSettingsSchema()
users_settings_schema = UserSettingsSchema(many=True)
user_settings_update_schema = UserSettingsSchema(partial=True)
