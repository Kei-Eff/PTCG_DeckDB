from flask import Blueprint, jsonify, request, url_for, render_template, redirect
from main import db
from models.deck import Deck
from schemas.deck_schema import deck_schema, decks_schema
from flask_login import login_required, current_user

decks = Blueprint("deck", __name__)

@decks.route("/my-decks/", methods=["GET"])
@login_required
def get_my_decks():
    data = {
        "decks": decks_schema.dump(Deck.query.filter_by(user_id=current_user.id))
    }
    return render_template("my_decks.html", page_data=data)


@decks.route("/decks/", methods=["GET"])
def get_decks():
    data = {
        "decks": decks_schema.dump(Deck.query.all())
    }
    return render_template("decks.html", page_data=data)

@decks.route("/deck/", methods=["GET", "POST"])
@login_required
def create_deck():
    if request.method == "GET":
        return render_template("create_deck.html")

    new_deck = deck_schema.load(request.form)
    new_deck.user = current_user
    db.session.add(new_deck)
    db.session.commit()
    return redirect(url_for("deck.get_my_decks"))

@decks.route("/decks/<int:id>/", methods=["GET"])
def get_deck(id):
    deck = Deck.query.get_or_404(id)
    return jsonify(deck.serialize)

@decks.route("/decks/<int:id>/", methods=["PUT", "PATCH"])
def update_deck(id):
    deck = Deck.filter_by(id=id)
    deck.update(dict(name=request.json["name"]))
    db.session.commit()
    return jsonify(deck.first().serialize)

@decks.route("/decks/<int:id>/", methods=["DELETE"])
def delete_deck(id):
    deck = Deck.query.get_or_404(id)
    db.session.delete(deck)
    db.session.commit()
    return jsonify(deck.serialize)

