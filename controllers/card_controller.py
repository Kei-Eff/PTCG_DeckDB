from flask import Blueprint, request, url_for, render_template, redirect, abort
from main import db
from models.card import Card
from models.deck import Deck
from schemas.card_schema import card_schema, cards_schema, card_update_schema
from schemas.deck_schema import deck_schema
from flask_login import login_required, current_user
from marshmallow import ValidationError

cards = Blueprint("card", __name__)

@cards.route("/deck/<int:id>/cards/", methods=["GET"])
@login_required
def get_cards_in_deck(id):
    deck = Deck.query.get_or_404(id)
    data = {
        "deck": deck_schema.dump(deck),
        "cards": cards_schema.dump(Card.query.filter_by(deck_id=id))
    }
    return render_template("cards.html", page_data=data)

# @cards.route("/card/", methods=["GET", "POST"])
# @login_required
# def create_card():
#     if request.method == "GET":
#         return render_template("create_card.html")

#     new_card = card_schema.load(request.form)
#     new_card.user = current_user
#     db.session.add(new_card)
#     db.session.commit()
#     return redirect(url_for("card.get_my_cards"))

# @cards.route("/card/<int:id>/", methods=["GET", "POST"])
# @login_required
# def update_card(id):
#     card = Card.query.get_or_404(id)
#     if current_user.id != card.user_id:
#         abort(403, "You do not have permission to alter this card.")

#     data = {
#         "card": card_schema.dump(card)
#     }

#     if request.method == "GET":
#         return render_template("edit_card.html", page_data=data)

#     card = Card.query.filter_by(id=id)
#     updated_fields = card_schema.dump(request.form)
#     errors = card_update_schema.validate(updated_fields)

#     if errors:
#         raise ValidationError(message=errors)

#     card.update(updated_fields)
#     db.session.commit()
#     return redirect(url_for("card.get_my_cards"))

# @cards.route("/card/<int:id>/delete/", methods=["POST"])
# @login_required
# def delete_card(id):
#     card = Card.query.get_or_404(id)
#     if current_user.id != card.user_id:
#         abort(403, "You do not have permission to delete this card.")
        
#     db.session.delete(card)
#     db.session.commit()
#     return redirect(url_for("card.get_my_cards"))
