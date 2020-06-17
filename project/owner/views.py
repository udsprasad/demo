from flask import Blueprint,render_template,redirect,url_for
from project import db
from project.owner.forms import Addform
from project.models import Owner
from flask_login import login_required

owner_blueprint=Blueprint('owner',__name__,template_folder='templates/owner')

@owner_blueprint.route('/add',methods=['GET','POST'])
@login_required
def add():
    form=Addform()
    if form.validate_on_submit():
        name=form.name.data
        puppy_id=form.puppy_id.data
        new = Owner(name,puppy_id)
        db.session.add(new)
        db.session.commit()
        return redirect(url_for('puppy.list'))

    return render_template('add_owner.html',form=form)
