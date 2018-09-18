import flask
import flask_login
import FormSignIn
import FormSignUp

view_account = flask.Blueprint(
    'view_account', __name__, template_folder='templates')


@view_account.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    form = FormSignIn.FormSignIn()
    if form.validate_on_submit():
        flask.flash('登录成功')
        return flask.redirect(flask.url_for('view_index.index'))
    return flask.render_template('Account/sign_in.html', t='登录', form=form)


@view_account.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form = FormSignUp.FormSignUp()
    if form.validate_on_submit():
        flask.flash('注册成功')
        return flask.redirect(flask.url_for('view_index.index'))
    return flask.render_template('Account/sign_up.html', t='注册', form=form)
