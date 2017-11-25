from start import create_app,db

if __name__ == '__main__':
    app = create_app()
    from init_db import init_db
    init_db(app,db)
    app.run()