from flask import Blueprint, jsonify, request, render_template, redirect, url_for, abort, current_app
from main import db
from models.decks import Deck
from schemas.deck_schema import deck_schema, decks_schema
from flask_login import login_required, current_user
import boto3

deck = Blueprint('deck', __name__)

@deck.route("/")
def homepage():
    data = {
        "page_title": "Homepage"
    }

    return render_template("homepage.html", page_data=data)