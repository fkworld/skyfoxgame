import flask
import flask_login

view_game = flask.Blueprint(
    'view_game', __name__, template_folder='templates')


@view_game.route('/jdqs', methods=['GET', 'POST'])
def jdqs():
    from forms.sign_in import FormSignIn
    form = FormSignIn()
    flask.flash('验证登录')
    if form.validate_on_submit():
        from models.user import User
        user = User(form.account.data, form.password.data)
        if user.check_password():
            login_user = user.check_password()
            flask_login.login_user(login_user, True)
            return flask.redirect('http://test.skyfoxgame.com/jdqs/')
        else:
            flask.flash('登录失败，请检查账号密码是否正确')
            return flask.redirect(flask.url_for('view_account.sign_in'))
    return flask.render_template('Account/sign_in.html', t='登录', form=form)
