from flask import Flask, render_template


def create_app():

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("homepage.html")


    @app.route("/profile")
    def profile():
        return "User's profile page."


    @app.route("/userdecks")
    def userdecks():
        return "List of decks added by a user."


    @app.route("/decks/<id>")
    def deck(id):
        return "Decklist for " + str(id)


    @app.route("/decks")
    def decks():
        return "List of decks added by all users on the site."


    @app.route("/userindex")
    def users():
        return "List of users registered on this website."


    @app.route("/cards")
    def cards():
        return "Card search page."

    if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)

    return app