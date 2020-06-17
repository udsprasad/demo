import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app=Flask(__name__)
login_manager = LoginManager()

Basedir=os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(Basedir,'data.sqlite')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.config['SECRET_KEY']="keyyy"

db=SQLAlchemy(app)

Migrate(app,db)

login_manager.init_app(app)
login_manager.login_view='login'


from project.puppy.views import puppy_blueprint
from project.owner.views import owner_blueprint

app.register_blueprint(puppy_blueprint,url_prefix='/puppy')
app.register_blueprint(owner_blueprint,url_prefix='/owner')
