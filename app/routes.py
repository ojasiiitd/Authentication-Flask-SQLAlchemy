from flask import render_template , flash , redirect , url_for , request
from app import app
from app.forms import RegForm , LoginForm
from app.models import User

@app.route('/')
def homepage():
    return render_template("information.html")

@app.route("/signup" , methods = ['GET' , 'POST'])
def signuppage() :
    form = RegForm(request.form)
    if request.method == "POST" and form.validate():
        if form.validate() :
            flash("Account created for %s!" % (form.uname.data) , "success")
            return redirect(url_for("homepage"))
        # else :
        #     flash("Sorry, account could not be created at this time" , "danger")
        #     return redirect(url_for("signuppage"))
    else :
        return render_template("signup.html" , form = form)

@app.route("/login" , methods = ['GET' , 'POST'])
def loginpage():
    form = LoginForm(request.form)
    return render_template("login.html" , form = form)
