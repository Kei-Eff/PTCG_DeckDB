from main import db

class UserSettings(db.Model):
    __tablename__ = "UserSettings"
    id = db.Column(db.Integer, primary_key=True)
    is_dark_mode = db.Column(db.Boolean(), default=False)
    is_anon_mode = db.Column(db.Boolean(), default=False)
    user_id = db.Column(db.Integer, db.ForeignKey("User.id"), nullable=False)

    def __init__(self, is_dark_mode = False, is_anon_mode = False):
        self.is_dark_mode = is_dark_mode
        self.is_anon_mode = is_anon_mode

    @property
    def serialize(self):
        return {
            "id": self.id,
            "is_dark_mode": self.is_dark_mode,
            "is_anon_mode": self.is_anon_mode
        }
