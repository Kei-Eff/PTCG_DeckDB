from flask import Blueprint, jsonify, request
from flask.templating import render_template
from main import db
from models.user import User

users = Blueprint('user', __name__)

@users.route('/users', methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize for user in users])

@users.route('/users', methods=["POST"])
def create_user():
    new_user = User(request.json["username"], request.json["password"], request.json["email"])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize)

@users.route('/users/<int:id>/', methods=["GET"])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.serialize)

@users.route('/users/<int:id>/', methods=["PUT", "PATCH"])
def update_user(id):
    user = User.filter_by(id=id)
    user.update(dict(password=request.json["password"]))
    user.update(dict(email=request.json["email"]))
    db.session.commit()
    return jsonify(user.first().serialize)

@users.route('/users/<int:id>/', methods=["DELETE"])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.serialize)
