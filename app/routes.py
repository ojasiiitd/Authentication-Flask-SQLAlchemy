from flask import render_template , flash , redirect , url_for , request
from app import app
from app.models import User

@app.route('/')
def homepage():
    return render_template("information.html")

@app.route("/login")
def loginpage():
    return render_template("information.html")

@app.route("/signup")
def signuppage() :
    return render_template("information.html")