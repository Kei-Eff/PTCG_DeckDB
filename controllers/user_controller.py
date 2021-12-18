from flask import Blueprint, request, render_template, jsonify
from main import db
from models.user import User
from schemas.user_schema import user_schema
from flask_login import login_required, current_user


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
    if request.method == "GET":
        return render_template("profile.html")
    
    # user = User.query.filter_by(id = current_user.id)
    # updated_fields = user.schema.dump(request.form)
    # errors = user_update_schema.validate(updated_fields)

    # if errors:
    #     raise ValidationError(message=errors)

    # user.update(updated_fields)
    # db.session.commit()
    return render_template("profile.html")

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
