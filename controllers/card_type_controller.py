from flask import Blueprint, jsonify, request
from main import db
from models.card_type import CardType

card_types = Blueprint("card_type", __name__)

@card_types.route("/card-types", methods=["GET"])
def get_card_types():
    card_types = CardType.query.all()
    return jsonify([card_type.serialize for card_type in card_types])

