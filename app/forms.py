from flask_wtf import FlaskForm
from wtforms import Form , StringField , PasswordField , SubmitField
from wtforms.validators import *

class RegForm(FlaskForm) :
    uname = StringField("Username" , validators=[
        DataRequired() ,
        Length(min=3 , max=20)])
    email = StringField("E-Mail" , validators=[
        DataRequired() ,
        Email()
    ])
    password = PasswordField("Password" , validators=[
        DataRequired()
    ])
    confirm = PasswordField("Confirm Password" , validators=[
        EqualTo('password') ,
        DataRequired()
    ])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm) :
    uname = StringField("Username" , validators=[
        DataRequired() ,
        Length(min=3 , max=20)])
    password = PasswordField("Password" , validators=[
        DataRequired()
    ])
    submit = SubmitField("Login")