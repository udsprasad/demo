from flask import Blueprint,render_template,url_for,redirect
from project import db
from project.models import Puppy
from project.puppy.forms import Addform,Delform
from flask_login import login_required

puppy_blueprint=Blueprint("puppy",__name__,template_folder='templates/puppy')


@puppy_blueprint.route('/add',methods=['GET','POST'])
@login_required
def add():
    form=Addform()
    if form.validate_on_submit():

        new_puppy=Puppy(form.name.data)
        db.session.add(new_puppy)
        db.session.commit()

        return redirect(url_for('puppy.list'))
    return render_template('add.html',form=form)

@puppy_blueprint.route('/list')
@login_required
def list():
    puppies=Puppy.query.all()
    return render_template('list.html',puppies=puppies)
