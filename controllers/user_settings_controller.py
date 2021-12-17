from flask import Blueprint, jsonify, request
from flask.templating import render_template
from main import db
from models.user_settings import UserSettings

user_settings = Blueprint('user_settings', __name__)

@user_settings.route('/user_settings', methods=["GET"])
def get_all_user_settings():
    user_settings = UserSettings.query.all()
    return jsonify([user_settings.serialize for user_settings in user_settings])

@user_settings.route('/user_settings', methods=["POST"])
def create_user_settings():
    new_user_settings = UserSettings(request.json["is_dark_mode"], request.json["is_anon_mode"])
    db.session.add(new_user_settings)
    db.session.commit()
    return jsonify(new_user_settings.serialize)

@user_settings.route('/user_settings/<int:id>/', methods=["GET"])
def get_user_settings(id):
    user_settings = UserSettings.query.get_or_404(id)
    return jsonify(user_settings.serialize)

@user_settings.route('/user_settings/<int:id>/', methods=["PUT", "PATCH"])
def update_user_settings(id):
    user_settings = UserSettings.filter_by(id=id)
    user_settings.update(dict(is_dark_mode=request.json["is_dark_mode"]))
    user_settings.update(dict(is_anon_mode=request.json["is_anon_mode"]))
    db.session.commit()
    return jsonify(user_settings.first().serialize)
