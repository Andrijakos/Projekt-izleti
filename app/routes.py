from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import LoginForm, RegistrationForm,TripForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Address, Trip
from werkzeug.urls import url_parse

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, surname=form.surname.data, username=form.username.data, email=form.email.data, cellphone=form.cellphone.data)  # Gdje je problem?
        user.set_password(form.password.data)
        address = Address()  #  provjerit da li adresa postoji ako da dodat id postojeće useru ako ne napravit novu i dodat id nove useru
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/create_trip', methods=['GET', 'POST'])
def make_trip():
    form = TripForm()
    if form.validate_on_submit():
        trip = Trip(trip_name=form.name.data, max_number=form.max_number.data, start_date=form.start_date.data, end_date=form.end_date.data, price=form.price.data, destination=form.destination.data,
                    trip_description=form.description.data)  # Kako dodati id usera?
        db.session.add(trip)
        db.session.commit()
        flash('Congratulations, you added your trip!')
        return redirect(url_for('trips'))
    return render_template('create_trip.html', title='Create Trip', form=form)
