from flask import Blueprint, jsonify, request
from flask.templating import render_template
from main import db
from models.card import Card

cards = Blueprint('card', __name__)

@cards.route('/')
def homepage():
    return render_template("homepage.html")

@cards.route('/cards', methods=["GET"])
def get_cards():
    cards = Card.query.all()
    return jsonify([card.serialize for card in cards])

@cards.route('/cards', methods=["POST"])
def create_card():
    new_card = Card(request.json["name"])
    db.session.add(new_card)
    db.session.commit()
    return jsonify(new_card.serialize)

@cards.route('/cards/<int:id>/', methods=["GET"])
def get_card(id):
    card = Card.query.get_or_404(id)
    return jsonify(card.serialize)

@cards.route('/cards/<int:id>/', methods=["PUT", "PATCH"])
def update_card(id):
    card = Card.filter_by(id=id)
    card.update(dict(name=request.json["name"]))
    db.session.commit()
    return jsonify(card.first().serialize)

@cards.route('/cards/<int:id>/', methods=["DELETE"])
def delete_card(id):
    card = Card.query.get_or_404(id)
    db.session.delete(card)
    db.session.commit()
    return jsonify(card.serialize)
