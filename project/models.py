from project import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model,UserMixin):
    id =db.Column(db.Integer,primary_key=True)
    email =db.Column(db.String(64),unique=True,index=True)
    username=db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self,email,username,password_hash):
        self.email=email
        self.username=username
        self.password_hash=generate_password_hash(password_hash)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)


class Puppy(db.Model):

    id = db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)

    owner=db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name):
        self.name=name


    def __repr__(self):
        if self.owner:
            return f"Puppy id: {self.id} Puppy name: {self.name} Owner name: {self.owner.name}"
        else:
            return f"No owner assigned for Puppy name ={self.name}"


class Owner(db.Model):

        id = db.Column(db.Integer,primary_key=True)
        name=db.Column(db.Text)

        puppy_id=db.Column(db.Integer,db.ForeignKey('puppy.id'))

        def __init__(self,name,puppy_id):
            self.name=name
            self.puppy_id=puppy_id
        def __repr__(self):
            return f"Owner name:{self.name} and Puppy id:{self.puppy_id}"
