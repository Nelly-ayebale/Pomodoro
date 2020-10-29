from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Todo,User
from .forms import TodoForm, UpdateProfile
import db,photos
from flask_login import login_required,current_user


@main.route('/')
def index():
    '''
    View root page that returns the index page and its data
    '''
    title = 'Pomodoro Tracker'
    render_template('index.html', title=title)

@main.route('/new_todo', methods=['GET','POST'])
@login_required
def new_todo():
    form = TodoForm()
    if form.validate_on_submit():
        category = form.category.data
        description = form.description.data
        user_id = current_user
        new_todo= Todo(category=category,description=description,user_id=current_user._get_current_object().id)
        new_todo.save_todos()

        return redirect(url_for('main.index'))
    return render_template('new_todo.html', form=form)
    
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))