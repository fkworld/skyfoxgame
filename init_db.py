from start import app, db
from ModelApp import App

with app.app_context():
    db.create_all()