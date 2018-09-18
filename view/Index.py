import flask

view_index = flask.Blueprint(
    'view_index', __name__, template_folder='templates')


@view_index.route('/')
def index():
    return flask.render_template('Home/index.html', t='首页')


@view_index.route('/game_center')
def game_center():
    return flask.render_template('Home/game_center.html', t='游戏中心')


@view_index.route('user_agreement')
def user_agreement():
    return flask.render_template('Home/user_agreement.html', t='用户协议')


@view_index.route('anti_addiction')
def anti_addiction():
    return flask.render_template('Home/anti_addiction.html', t='防沉迷')


@view_index.route('parental_controls')
def parental_controls():
    return flask.render_template('Home/parental_controls.html', t='家长监护')


@view_index.route('dispute_handling')
def dispute_handling():
    return flask.render_template('Home/dispute_handling.html', t='纠纷处理')


@view_index.route('customer_service_center')
def customer_service_center():
    return flask.render_template('Home/customer_service_center.html', t='客服中心')


@view_index.route('/contact_us')
def contact_us():
    return flask.render_template('Home/contact_us.html', t='联系我们')


@view_index.route('/sign_in')
def sign_in():
    return flask.redirect(flask.url_for('view_account.sign_in'))


@view_index.route('/sign_up')
def sign_up():
    return flask.redirect(flask.url_for('view_account.sign_up'))


@view_index.route('/privacy_policy')
def privacy_policy():
    return flask.render_template('Home/privacy_policy.html', t='首页')
