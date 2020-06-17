from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField,validators

class Addform(FlaskForm):

   name=StringField("Enter the Owner name:",[validators.Required()])

   puppy_id=IntegerField("Enter the puppy id:",[validators.Required()])
   
   submit=SubmitField("Submit")
