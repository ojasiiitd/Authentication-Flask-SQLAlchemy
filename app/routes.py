from flask import render_template , flash , redirect , url_for , request
from app import app
from app.forms import RegForm , LoginForm
from app.models import User
from app import app, db, pwd
from flask_login import login_user , current_user , logout_user , login_required

@app.route('/')
def homepage():
    return render_template("information.html" , )

@app.route("/signup" , methods = ['GET' , 'POST'])
def signuppage() :
    if current_user.is_authenticated :
        flash("You are already logged in." , "warning")
        return redirect(url_for("homepage"))
    form = RegForm(request.form)
    if request.method == "POST" and form.validate():
        hashed = pwd.generate_password_hash(form.password.data).decode('utf-8')
        element = User(uname = form.uname.data , email = form.email.data , password = hashed)
        db.session.add(element)
        db.session.commit()
        flash("Account created for %s!" % (form.uname.data) , "success")
        return redirect(url_for("loginpage"))
    return render_template("signup.html" , form = form)

@app.route("/login" , methods = ['GET' , 'POST'])
def loginpage():
    if current_user.is_authenticated :
        flash("You are already logged in." , "warning")
        return redirect(url_for("homepage"))
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        member = User.query.filter_by(uname = form.uname.data).first()
        if member and pwd.check_password_hash(member.password , form.password.data) :
            login_user(member)
            flash("Welcome, %s!" % (form.uname.data) , "success")
            return redirect(url_for("homepage"))
        else :
            flash("Username or Password doesn't match, please try again." , "danger")
            return redirect(url_for("loginpage"))
    return render_template("login.html" , form = form)

@app.route("/logout")
def logoutpage():
    logout_user()
    flash("Successfuly logged out." , "success")
    return redirect(url_for("homepage"))

@app.route("/member-page")
@login_required
def member():
    return render_template("members.html")