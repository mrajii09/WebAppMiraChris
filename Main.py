# Title: VitelloWeb
# Authors: Miraj Acharya, Christopher Shane Rocco Vitello
# December 2025

from flask import Flask, render_template, redirect, url_for
import sqlalchemy


app = Flask(__name__)

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

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/purchases')
def purchase():
    return render_template("purchases.html")

if __name__ == '__main__':
    app.run(debug=True)
