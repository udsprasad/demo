from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from project.models import User


class Loginform(FlaskForm):

      email=StringField("Email:",validators=[DataRequired(),Email()])
      password=PasswordField("Password",validators=[DataRequired()])
      submit=SubmitField("Log in")





class Registerform(FlaskForm):

   email=StringField("Email:",validators=[DataRequired(),Email()])
   username=StringField("Username:",validators=[DataRequired()])
   password=PasswordField("Password",validators=[DataRequired(),EqualTo('cnf_pass',message="Password must match!")])
   cnf_pass=PasswordField("Confirm Password",validators=[DataRequired()])
   submit=SubmitField("Register!")

   def validate_email(self,email):
       if User.query.filter_by(email=self.email.data).first():
           raise ValidationError('Email has been registered')
   def validate_username(self,username):
       if User.query.filter_by(username=self.username.data).first():
           raise ValidationError('Username has been registered')
