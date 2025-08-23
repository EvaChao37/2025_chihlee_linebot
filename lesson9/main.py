from flask import Flask

app = Flask(__name__)

@app.route("/")
def intex():
    return "<p>Hello, Flask!</p>"

@app.route("/name")
def my_anme():
    return "My name is <H1>Eva<H1>"