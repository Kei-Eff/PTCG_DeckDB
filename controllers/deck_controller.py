from flask import Blueprint, request, url_for, render_template, redirect, abort
from main import db
from models.deck import Deck
from models.card import Card
from schemas.deck_schema import deck_schema, decks_schema, deck_update_schema
from flask_login import login_required, current_user
from marshmallow import ValidationError
from sqlalchemy import func

decks = Blueprint("deck", __name__)

@decks.route("/decks/", methods=["GET"])
def get_decks():
    data = {
        "decks": decks_schema.dump(Deck.query.order_by(Deck.date_created.desc()).all())
    }
    return render_template("decks.html", page_data=data)
    
@decks.route("/decks/<int:id>/", methods=["GET"])
def get_deck(id):
    deck = Deck.query.get_or_404(id)
    total_cards = Card.query.with_entities(func.sum(Card.quantity)).filter_by(deck_id=deck.id).scalar()
    data = {
        "deck": deck_schema.dump(deck),
        "total_cards": total_cards
    }

    return render_template("deck.html", page_data=data)
    
@decks.route("/my-decks/", methods=["GET"])
@login_required
def get_my_decks():
    data = {
        "decks": decks_schema.dump(Deck.query.filter_by(user_id=current_user.id).order_by(Deck.date_created.desc()))
    }
    return render_template("my_decks.html", page_data=data)

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

@decks.route("/deck/<int:id>/", methods=["GET", "POST"])
@login_required
def update_deck(id):
    deck = Deck.query.get_or_404(id)
    if current_user.id != deck.user_id:
        abort(403, "You do not have permission to alter this deck.")

    data = {
        "deck": deck_schema.dump(deck)
    }

    if request.method == "GET":
        return render_template("edit_deck.html", page_data=data)

    deck = Deck.query.filter_by(id=id)
    updated_fields = deck_schema.dump(request.form)
    errors = deck_update_schema.validate(updated_fields)

    if errors:
        raise ValidationError(message=errors)

    deck.update(updated_fields)
    db.session.commit()
    return redirect(url_for("deck.get_my_decks"))

@decks.route("/deck/<int:id>/delete/", methods=["POST"])
@login_required
def delete_deck(id):
    deck = Deck.query.get_or_404(id)
    if current_user.id != deck.user_id:
        abort(403, "You do not have permission to delete this deck.")
        
    db.session.delete(deck)
    db.session.commit()
    return redirect(url_for("deck.get_my_decks"))
