import flask
import flask_login
import flask_sqlalchemy

app = flask.Flask(__name__)
app.secret_key = '42'

# 路由
from views.account import view_account
from views.index import view_index
app.register_blueprint(view_index, url_prefix='')
app.register_blueprint(view_account, url_prefix='/account')

# flask_sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account_server.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = flask_sqlalchemy.SQLAlchemy(app)

# flask_login
login_manager = flask_login.LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
    if user_id == 'None':
        return None
    from models.user import User
    return User.query.get(int(user_id))


# run
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
