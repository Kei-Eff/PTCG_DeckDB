from flask import Blueprint
from flask.templating import render_template

home = Blueprint('home', __name__)

@home.route('/', methods=["GET"])
def homepage():
    return render_template("homepage.html")

@home.route('/signup', methods=["GET"])
def signup():
    return render_template("signup.html")

@home.route('/login', methods=["GET"])
def login():
    return render_template("login.html")
