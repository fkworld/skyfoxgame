from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '42'
    app.debug = True

    from index_view import index_view
    from product_view import product_view
    app.register_blueprint(index_view, url_prefix='/')
    app.register_blueprint(index_view, url_prefix='/product')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()