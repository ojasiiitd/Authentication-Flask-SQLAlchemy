from datetime import datetime
from app import db

class User(db.Model) :
    sno = db.Column(db.Integer , primary_key = True)
    time = db.Column(db.DateTime , default = datetime.now)
    uname = db.Column(db.String(20) , unique = True , nullable = False)
    email = db.Column(db.String(50) , unique = True , nullable = False)
    password = db.Column(db.String(100) , nullable = False)

    def __repr__(self):
        return  'User(%s , %s)' % (self.uname , self.email)

# from app import db
# db.create_all()   
# from app import User
# elt = User(uname = "ojas" , email = "ojas@gmail.com" , password = "johncena")
# db.session.add(elt)
# db.session.commit()
# User.query.all()