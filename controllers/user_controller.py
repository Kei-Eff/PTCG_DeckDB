from flask import Blueprint, request, render_template, jsonify, redirect, url_for
from main import db
from models.user import User
from models.user_settings import UserSettings
from schemas.user_settings_schema import user_settings_schema, user_settings_update_schema
from schemas.user_schema import user_schema
from flask_login import login_required, current_user
from marshmallow import ValidationError


users = Blueprint("user", __name__)


# @users.route("/users", methods=["GET"])
# def get_users():
#     users = User.query.all()
#     return jsonify([user.serialize for user in users])


# @users.route("/users/<int:id>/", methods=["GET"])
# def get_user(id):
#     user = User.query.get_or_404(id)
#     return jsonify(user.serialize)

@users.route("/profile", methods=["GET", "POST"])
@login_required
def user_detail():
    current_user_settings = UserSettings.query.filter_by(user_id = current_user.id)
    data = {
        "settings": current_user_settings.first()
    }
    if request.method == "GET":
        return render_template("profile.html", page_data=data)

    updated_fields = user_settings_schema.dump(request.form)
    errors = user_settings_update_schema.validate(updated_fields)

    if errors:
        raise ValidationError(message=errors)

    current_user_settings.update(updated_fields)
    db.session.commit()
    return redirect(url_for("home.homepage"))

@users.route("/users/<int:id>/", methods=["PUT", "PATCH"])
def update_user(id):
    user = User.filter_by(id=id)
    user.update(dict(password=request.json["password"]))
    user.update(dict(email=request.json["email"]))
    db.session.commit()
    return jsonify(user.first().serialize)

@users.route("/users/<int:id>/", methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.serialize)
