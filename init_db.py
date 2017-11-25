from start import app, db
from ModelApp import App

def init_db():
    with app.app_context():
        db.create_all()