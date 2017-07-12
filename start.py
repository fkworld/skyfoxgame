from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '42'
    app.debug = True

    from index_view import index_view
    from app_view import app_view
    app.register_blueprint(index_view, url_prefix='/')
    app.register_blueprint(app_view, url_prefix='/app')

    return app

app = create_app()

if __name__ == '__main__':
    # app = create_app() # gunicorn方式启动需要把这句话放在外面
    app.run()