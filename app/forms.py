from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateTimeField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length, Email, EqualTo
from app.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=50)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    surname = StringField('Surname', validators=[DataRequired(), Length(min=2, max=20)])
    cellphone = IntegerField('Cellphone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])#kako razdijelit adresu na ulicu i broj??
    city = StringField('City', validators=[DataRequired()])
    zipcode = IntegerField('Zipcode', validators=[DataRequired()]) #da li će radit samo ovako?
    country = StringField('Country', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class TripForm(FlaskForm):
    name = StringField('Tripname', validators=[DataRequired(), Length(min=2, max=128)])
    destination = StringField('Destination', validators=[DataRequired(), Length(min=2, max=64)])
    max_number = IntegerField('Max number', validators=[DataRequired(), Length(min=1)])
    start_date = DateTimeField('Start date', validators=[DataRequired()])
    end_date = DateTimeField('End date', validators=[DataRequired()])
    description = TextAreaField('Trip description', validators=[DataRequired(), Length(max=1000)])  #vidit textareafield dal će valjat
    price = IntegerField('Price', validators=[DataRequired()])
