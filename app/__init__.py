from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config["SQLALCHEMY_DATABSE_URI"] = "sqlite:///info.db"
db = SQLAlchemy(app)
pwd = Bcrypt(app)

from app import routes