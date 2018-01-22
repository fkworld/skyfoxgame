from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class


def create_app():
    """初始化网站的app
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '42'
    app.debug = True

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)

    app.config['UPLOADS_DEFAULT_DEST'] = 'uploads'
    configure_uploads(app, appimages)
    patch_request_class(app, 1024 * 1024 * 1024)

    from viewindex import view_index
    from viewapp import view_app
    from viewadmin import view_admin
    app.register_blueprint(view_index, url_prefix='')  # 注意此处不能为'/'，应为空
    app.register_blueprint(view_app, url_prefix='/app')
    app.register_blueprint(view_admin, url_prefix='/ilovefangchunpin')

    return app


# 初始化数据库，上传限制
db = SQLAlchemy()
appimages = UploadSet('APPIMAGES', IMAGES)
# 调用函数对app进行初始化，gunicorn方式启动需要把这句话放在外面
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
