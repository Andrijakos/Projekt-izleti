from app import app, db
from app.models import User, Trip, TripUser



@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'TripUser': TripUser, 'Trip': Trip}
