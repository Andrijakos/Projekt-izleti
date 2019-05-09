import os
import secrets
from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, TripForm, EditProfileForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Trip
from werkzeug.urls import url_parse
from datetime import datetime, timedelta


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


def save_user_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_ff = random_hex + f_ext
    picture_path = os.path.join('static/avatars', picture_ff)
    form_picture.save(picture_path)

    return picture_ff

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    user = User()
    if form.validate_on_submit():

        if form.picture.data:
            picture_file = save_user_picture(form.picture.data)
            user.image_file = picture_file
        user.name = form.name.data
        user.surname = form.surname.data
        user.username = form.username.data
        user.email = form.email.data
        user.address = form.address.data
        user.postal_number = form.zipcode.data
        user.city = form.city.data
        user.country = form.country.data
        user.tel_number = form.cellphone.data
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
'''
Bootstrap(app)
class MyForm(Form):
    date = DateField(id='datepick')
'''




'''
Bootstrap(app)
class MyForm(Form):
    date = DateField(id='datepick')
'''

# funkcija za spremanje(i renaming) uploadane slike
def save_trip_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join('static/trip_pics', picture_fn)
    form_picture.save(picture_path)

    return picture_fn


@app.route('/create_trip', methods=['GET', 'POST'])
@login_required
def create_trip():
    form = TripForm()
    # form1 = MyForm()
    trip = Trip()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_trip_picture(form.picture.data)
            trip.image_file = picture_file
        '''    
        if trip.start_date > trip.end_date:
            flash('Ne moš se vratit prije no što kreneš')
            return redirect(url_for('create_trip'))
        '''
        trip.trip_name = form.name.data
        trip.destination = form.destination.data
        trip.max_number = form.max_number.data
        trip.start_date = form.start_date.data
        trip.end_date = form.end_date.data
        trip.trip_description = form.description.data
        trip.price = form.price.data
        trip.id_user = current_user.id
        # import pdb; pdb.set_trace()
        db.session.add(trip)
        db.session.commit()

        flash('Congratulations, you added your trip!', 'success')
        return redirect(url_for('index'))
    return render_template('create_trip.html', title='Create Trip', form=form)


@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    #  tu će ići Trips
    return render_template('user.html', user=user)   # dodat trips=trips


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.surname = form.surname.data
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.address = form.address.data
        current_user.postal_number = form.zipcode.data
        current_user.city = form.city.data
        current_user.country = form.country.data
        current_user.tel_number = form.cellphone.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('user', username=current_user.username))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.surname.data = current_user.surname
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.address.data = current_user.address
        form.zipcode.data = current_user.postal_number
        form.city.data = current_user.city
        form.country.data = current_user.country
        form.cellphone.data = current_user.tel_number
    return render_template('edit_profile.html', title='Edit Profile',
                           form=form)

'''
# OVO DORADITI NE VALJA!!
@app.route('/trip')
def trip(id):
    trip = Trip.filter(id=id)
    return render_template('trip.html', id=)

'''


# dekorator za last seen ako ćemo ubacit
'''
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
'''