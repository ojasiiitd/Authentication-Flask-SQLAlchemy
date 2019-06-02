from flask import render_template , flash , redirect , url_for , request
from app import app
from app.forms import RegForm , LoginForm
from app.models import User

@app.route('/')
def homepage():
    return render_template("information.html")

@app.route("/signup" , methods = ['GET' , 'POST'])
def signuppage() :
    form = RegForm()
    if request.method == "POST" and form.validate_on_submit() :
        flash('Account created for %s !' % (form.uname.data))
    return render_template("signup.html" , form = form)

@app.route("/login" , methods = ['GET' , 'POST'])
def loginpage():
    form = LoginForm()
    return render_template("login.html" , form = form)
