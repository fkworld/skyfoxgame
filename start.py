import flask

import view.Index
import view.Account

app = flask.Flask(__name__)
app.secret_key = '42'

# 路由
app.register_blueprint(view.Index.view_index, url_prefix='')
app.register_blueprint(view.Account.view_account, url_prefix='/account')

# run
if __name__ == '__main__':
    app.run(debug=True)

