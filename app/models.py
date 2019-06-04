from datetime import datetime
from app import db , login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model , UserMixin) :
    sno = db.Column(db.Integer , primary_key = True)
    time = db.Column(db.DateTime , default = datetime.now)
    uname = db.Column(db.String(20) , unique = True , nullable = False)
    email = db.Column(db.String(50) , unique = True , nullable = False)
    password = db.Column(db.String(60) , nullable = False)

    def __repr__(self):
        return  'User(%s , %s)' % (self.uname , self.email)