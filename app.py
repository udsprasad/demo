from project import app,db
from flask import render_template,redirect,url_for,flash,request,abort
from flask_login import login_user,login_required,logout_user
from project.models import User
from project.forms import Loginform,Registerform

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template('welcome.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you logged out')
    return render_template('home.html')

@app.route('/login',methods=['GET','POST'])
def login():

  form=Loginform()
  if form.validate_on_submit():

     user=User.query.filter_by(email=form.email.data).first()

     if user.check_password(form.password.data) and user is not None:

         login_user(user)
         flash('Logged in successfully!')

         next=request.args.get('next')
         if next == None or not next[0] =='/':
                next =url_for('welcome_user')

         return redirect(next)
  return render_template('login.html',form=form)

@app.route('/register',methods=['GET','POST'])
def register():
    form =Registerform()
    if form.validate_on_submit():
        user =User(form.email.data,form.username.data,form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for register')
        return redirect(url_for('login'))
    return render_template('register.html',form=form)












if __name__=='__main__':
    app.run(debug=True)
