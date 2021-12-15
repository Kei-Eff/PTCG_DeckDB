from flask import Flask, render_template


def create_app():

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("homepage.html")


    @app.route("/profile")
    def profile():
        return render_template("profile.html")


    @app.route("/userdecks")
    def userdecks():
        return "List of decks added by a user."


    @app.route("/decks/<id>")
    def deck(id):
        return "Decklist for " + str(id)


    @app.route("/decks")
    def decks():
        return render_template("decks.html")


    @app.route("/userindex")
    def users():
        return "List of users registered on this website."


    @app.route("/cards")
    def cards():
        return "Card search page."


    @app.route("/login")
    def login():
        return render_template("login.html")


    if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)

    return app