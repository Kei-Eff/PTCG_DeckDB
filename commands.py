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
