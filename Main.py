from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>ORDER AWAY<h1>\n This is an order app.'

@app.route('/admin')
def admin():
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
