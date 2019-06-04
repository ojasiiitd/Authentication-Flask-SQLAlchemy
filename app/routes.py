from flask import render_template , flash , redirect , url_for , request
from app import app
from app.forms import RegForm , LoginForm
from app.models import User
from app import app, db, pwd

@app.route('/')
def homepage():
    return render_template("information.html")

@app.route("/signup" , methods = ['GET' , 'POST'])
def signuppage() :
    form = RegForm(request.form)
    if request.method == "POST" and form.validate():
        hashed = pwd.generate_password_hash(form.password.data).decode('utf-8')
        element = User(uname = form.uname.data , email = form.email.data , password = hashed)
        db.session.add(element)
        db.session.commit()
        flash("Account created for %s!" % (form.uname.data) , "success")
        return redirect(url_for("loginpage"))
    else :
        return render_template("signup.html" , form = form)

@app.route("/login" , methods = ['GET' , 'POST'])
def loginpage():
    form = LoginForm(request.form)
    if request.method == "POST" :
        if form.validate() :
            flash("Welcome, %s!" % (form.uname.data) , "success")
            return redirect(url_for("homepage"))
        else :
            flash("Username or Password doesn't match, please try again." , "danger")
            return redirect(url_for("loginpage"))
    return render_template("login.html" , form = form)
