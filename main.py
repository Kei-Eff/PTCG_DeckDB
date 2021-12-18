import os
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


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

    # app.config.from_object("config.app_config")

    db.init_app(app)

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

    return app
