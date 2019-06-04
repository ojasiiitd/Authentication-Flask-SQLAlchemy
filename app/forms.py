from wtforms import Form , StringField , PasswordField , SubmitField , validators
from app.models import User

class RegForm(Form) :
    uname = StringField("Username" , validators=[
        validators.DataRequired() ,
        validators.Length(min=4 , message = "Username must be at least 6 characters long.")
    ])
    email = StringField("E-Mail" , validators=[
        validators.DataRequired() ,
        validators.Email() ,
        validators.Length(min=6 , message = "Email Address must be at least 6 characters long.")
    ])
    password = PasswordField("Password" , validators=[
        validators.DataRequired() ,
        validators.Length(min=4 , message = "Password must be at least 4 characters long.")
    ])
    confirm = PasswordField("Confirm Password" , validators=[
        validators.EqualTo('password' , message = "Passwords do not match.") ,
        validators.DataRequired()
    ])
    submit = SubmitField("Sign Up")

    def validate_uname(self , uname) :
        present = User.query.filter_by(uname = uname.data).first()
        if present:
            raise validators.ValidationError("This username has already been taken, please choose a different one.")
    
    def validate_email(self , email) :
        present = User.query.filter_by(email = email.data).first()
        if present:
            raise validators.ValidationError("This email has already been registered with us, please enter a different one.")

class LoginForm(Form) :
    uname = StringField("Username" , validators=[
        validators.DataRequired() ,
        validators.Length(min=4 , max=20)
    ])
    password = PasswordField("Password" , validators=[
        validators.DataRequired() ,
        validators.Length(min=4 , max=20)
    ])
    submit = SubmitField("Login")