import os
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow.exceptions import ValidationError


db = SQLAlchemy()
ma = Marshmallow()

def create_app():

    (
        db_user,
        db_pass,
        db_name,
        db_domain
    ) = (os.environ.get(item) for item in [
        "DB_USER",
        "DB_PASS",
        "DB_NAME",
        "DB_DOMAIN"
    ]
    )

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_domain}/{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config.from_object("config.app_config")

    db.init_app(app)
    ma.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)


    @app.route("/")
    def home():
        return render_template("homepage.html")

    @app.route("/profile")
    def profile():
        return render_template("profile.html")

    @app.route("/user_decks")
    def user_decks():
        return render_template("user_decks.html")

    @app.route("/decks/<id>/")
    def deck(id):
        return render_template("deck.html")

    @app.route("/decks")
    def decks():
        return render_template("decks.html")

    @app.route("/decks/new/")
    def create_deck():
        return render_template("create_deck.html")

    @app.route("/user_index")
    def users():
        return "List of users registered on this website."

    @app.route("/cards")
    def cards():
        return "Card search page."

    @app.route("/decks/<id>/add_card/")
    def add_card(id):
        return render_template("add_card.html")

    @app.route("/login")
    def login():
        return render_template("login.html")
    

    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(erorr.messages), 400)


    if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)

    return app
