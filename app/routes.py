from flask import render_template
from app import app
import datetime


@app.route('/')
@app.route('/index/')
def index():

    return render_template('index.html', title='Home')