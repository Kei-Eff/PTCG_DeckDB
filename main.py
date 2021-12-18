import os
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from marshmallow.exceptions import ValidationError


db = SQLAlchemy()
ma = Marshmallow()
lm = LoginManager()

def create_app():

    (
        db_user,
        db_pass,
        db_name,
        db_domain,
        secret_key
    ) = (os.environ.get(item) for item in [
        "DB_USER",
        "DB_PASS",
        "DB_NAME",
        "DB_DOMAIN",
        "SECRET_KEY"
    ]
    )

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_domain}/{db_name}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = secret_key

    # app.config.from_object("config.app_config")

    db.init_app(app)
    lm.init_app(app)

    from commands import db_commands
    app.register_blueprint(db_commands)

    # @app.route("/user_index")
    # def users():
    #     return "List of users registered on this website."

    # @app.route("/cards")
    # def cards():
    #     return "Card search page."

    # @app.errorhandler(ValidationError)
    # def handle_bad_request(error):
    #     return (jsonify(erorr.messages), 400)

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)

    @app.errorhandler(ValidationError)
    def handle_bad_request(error):
        return (jsonify(error.messages), 400)

    return app
