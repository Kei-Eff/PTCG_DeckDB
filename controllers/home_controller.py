from flask import Blueprint, request, render_template, redirect, url_for, abort
from main import db, lm
from models.user import User
from models.user_settings import UserSettings
from schemas.user_schema import user_schema
from flask_login import login_user, logout_user, login_required

@lm.user_loader
def load_user(user):
    return User.query.get(user)

@lm.unauthorized_handler
def unauthorized():
    return redirect("/login")

home = Blueprint("home", __name__)

@home.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html")

@home.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    new_user = user_schema.load(request.form)
    db.session.add(new_user)

    new_user_settings = UserSettings()
    new_user_settings.user = new_user
    db.session.add(new_user_settings)

    db.session.commit()
    login_user(new_user)
    return redirect(url_for("home.homepage"))

@home.route("/login", methods=["GET", "POST"])
def log_in():
    data = {"page_title": "Login"}

    if request.method =="GET":
        return render_template("login.html", page_data = data)

    user = User.query.filter_by(username=request.form["username"]).first()
    if user and user.check_password(password=request.form["password"]):
        login_user(user)
        return redirect(url_for("home.homepage"))

    abort(401, "Login failed. Please enter correct username and password.")

@home.route("/logout", methods=["POST"])
@login_required
def log_out():
    logout_user()
    return redirect(url_for("home.homepage"))