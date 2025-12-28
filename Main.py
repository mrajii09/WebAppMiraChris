# Title: VitelloWeb
# Authors: Miraj Acharya, Christopher Shane Rocco Vitello
# December 2025

from flask import Flask, render_template, request, redirect, url_for, session
import sqlalchemy
import flask_login

app = Flask(__name__)

app.secret_key = "Test123" # Enables ude of sessions,
# Test123 is a TEST VALUE, CHANGE LATER!!!!!!!

admin = False


# Home page
@app.route("/")
def home():
    return render_template("home.html")


# About page
@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/admin')
def admin():
    return redirect(url_for("home"))

# URL for login AND
# had GET --> user opens page
# and POST --> user submits form
@app.route('/login', methods=['GET', 'POST'])
def login():

    # IF user clicked the login button,
    # take the username and password they submitted
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        # UNFINISHED !!!!!!
    return render_template("login.html")


@app.route('/purchases')
def purchase():
    return render_template("purchases.html")


if __name__ == '__main__':
    app.run(debug=True)
