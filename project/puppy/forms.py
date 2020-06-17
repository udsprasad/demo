##puppy-->forms##
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,validators

class Addform(FlaskForm):

   name=StringField("Enter the puppy name:",[validators.Required()])
   submit=SubmitField("Submit")

class Delform(FlaskForm):

   id=IntegerField("Enter the puppy id:",[validators.Required()])
   submit=SubmitField("Submit")
