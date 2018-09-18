import flask
import flask_login

import view.Index
import view.Account

app = flask.Flask(__name__)
app.secret_key = '42'

# 路由
app.register_blueprint(view.Index.view_index, url_prefix='')
app.register_blueprint(view.Account.view_account, url_prefix='/account')

# flask_login
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return None


# run
app.run(debug=True)
