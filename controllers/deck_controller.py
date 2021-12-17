from flask import Blueprint, jsonify, request
from flask.templating import render_template
from main import db
from models.deck import Deck

decks = Blueprint('deck', __name__)

@decks.route('/')
def homepage():
    return render_template("homepage.html")

@decks.route('/decks', methods=["GET"])
def get_decks():
    decks = Deck.query.all()
    return jsonify([deck.serialize for deck in decks])

@decks.route('/decks', methods=["POST"])
def create_deck():
    new_deck = Deck(request.json["name"])
    db.session.add(new_deck)
    db.session.commit()
    return jsonify(new_deck.serialize)

@decks.route('/decks/<int:id>/', methods=["GET"])
def get_deck(id):
    deck = Deck.query.get_or_404(id)
    return jsonify(deck.serialize)

@decks.route('/decks/<int:id>/', methods=["PUT", "PATCH"])
def update_deck(id):
    deck = Deck.filter_by(id=id)
    deck.update(dict(name=request.json["name"]))
    db.session.commit()
    return jsonify(deck.first().serialize)

@decks.route('/decks/<int:id>/', methods=["DELETE"])
def delete_deck(id):
    deck = Deck.query.get_or_404(id)
    db.session.delete(deck)
    db.session.commit()
    return jsonify(deck.serialize)

