from flask import Flask , render_template , flash , redirect , url_for , request , logging
from flask-sqlalchemy import SQLAlchemy

app = Flask(__name__)
