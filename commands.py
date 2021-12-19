from main import db
from flask import Blueprint

db_commands = Blueprint("db-custom", __name__)

@db_commands.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created!")


@db_commands.cli.command("drop")
def drop_db():
    db.drop_all()
    db.engine.execute("DROP TABLE IF EXISTS alembic_version;")
    print("Tables deleted")


@db_commands.cli.command("seed")
def seed_db():
    from models.card_type import CardType

    card_types = ["Pokémon", "Trainer", "Energy"]

    for type in card_types:
        card_type = CardType(type)
        db.session.add(card_type)

    db.session.commit()
    print("CardTypes seeded")

@db_commands.cli.command("reset")
def reset_db():
    drop_db()
    seed_db()

@db_commands.cli.command("export")
def export_db():
    
    import json
    from models.user import User
    from models.user_settings import UserSettings
    from models.deck import Deck
    from models.card import Card
    from models.card_type import CardType
    from schemas.user_schema import users_schema
    from schemas.user_settings_schema import users_settings_schema
    from schemas.deck_schema import decks_schema
    from schemas.card_schema import cards_schema
    from schemas.card_type_schema import card_types_schema

    with open('export.txt', 'w') as f:
        users = users_schema.dump(User.query.all())
        f.write('USERS\n')
        f.write(json.dumps(users) + '\n')
        
        user_settings = users_settings_schema.dump(UserSettings.query.all())
        f.write('USER_SETTINGS\n')
        f.write(json.dumps(user_settings) + '\n')

        decks = decks_schema.dump(Deck.query.all())
        f.write('DECKS\n')
        f.write(json.dumps(decks) + '\n')

        cards = cards_schema.dump(Card.query.all())
        f.write('CARDS\n')
        f.write(json.dumps(cards) + '\n')

        card_types = card_types_schema.dump(CardType.query.all())
        f.write('CARD_TYPES\n')
        f.write(json.dumps(card_types) + '\n')
