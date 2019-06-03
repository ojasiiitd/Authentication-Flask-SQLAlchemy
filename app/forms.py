from wtforms import Form , StringField , PasswordField , SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegForm(Form) :
    uname = StringField("Username" , validators=[
        DataRequired() ,
        Length(min=4)
    ])
    email = StringField("E-Mail" , validators=[
        DataRequired() ,
        Email() ,
        Length(min=7)
    ])
    password = PasswordField("Password" , validators=[
        DataRequired() ,
        Length(min=4 , max=20)
    ])
    confirm = PasswordField("Confirm Password" , validators=[
        EqualTo('password') ,
        DataRequired()
    ])
    submit = SubmitField("Sign Up")

class LoginForm(Form) :
    uname = StringField("Username" , validators=[
        DataRequired() ,
        Length(min=4 , max=20)
    ])
    password = PasswordField("Password" , validators=[
        DataRequired() ,
        Length(min=4 , max=20)
    ])
    submit = SubmitField("Login")