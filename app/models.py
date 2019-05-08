from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    surname = db.Column(db.String(64), index=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    address = db.Column(db.String(64), index=True)
    postal_number = db.Column(db.Integer, index=True)
    city = db.Column(db.String(64), index=True)
    country = db.Column(db.String(64), index=True)
    tel_number = db.Column(db.String(64), index=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

'''
TripUser = Table('TripUser',
    Column('id', Integer, primary_key=True),
    Column('id_user', Integer, ForeignKey('user.id')),
    Column('id_trip', Integer, ForeignKey('trip.id')))
    '''


class TripUser(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trip.id'), primary_key=True)


class Trip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    trip_name = db.Column(db.String(128), index=True)
    destination = db.Column(db.String(64), index=True)
    max_number = db.Column(db.String, index=True)
    start_date = db.Column(db.DateTime, index=True)
    end_date = db.Column(db.DateTime, index=True)
    trip_description = db.Column(db.Text(1000), index=True)
    price = db.Column(db.String, index=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Trip {}>'.format(self.trip_name)


@login.user_loader


def load_user(id):
    return User.query.get(int(id))
