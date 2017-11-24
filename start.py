from flask import Flask
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '42'
    app.debug = True

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    from index_view import index_view
    from app_view import app_view
    app.register_blueprint(index_view, url_prefix='') # 注意此处不能为'/'，应为空
    app.register_blueprint(app_view, url_prefix='/app')

    return app

db = SQLAlchemy()
app = create_app()

if __name__ == '__main__':
    # app = create_app() # gunicorn方式启动需要把这句话放在外面
    app.run()