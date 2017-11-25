def init_db(app,db):
    with app.app_context():
        db.create_all()