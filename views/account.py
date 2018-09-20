import flask
import flask_login

view_account = flask.Blueprint(
    'view_account', __name__, template_folder='templates')


@view_account.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    from forms.sign_in import FormSignIn
    form = FormSignIn()
    if form.validate_on_submit():
        from models.user import User
        user = User(form.account.data, form.password.data)
        if user.check_password():
            login_user = user.check_password()
            flask_login.login_user(login_user, True)
            flask.flash('登录成功')
            return flask.redirect(flask.request.args.get('next') or flask.url_for('view_index.index'))
        else:
            flask.flash('登录失败，请检查账号密码是否正确')
            return flask.redirect(flask.url_for('view_account.sign_in'))
    return flask.render_template('Account/sign_in.html', t='登录', form=form)


@view_account.route('/sign_out', methods=['GET', 'POST'])
@flask_login.login_required
def sign_out():
    flask_login.logout_user()
    flask.flash('登出成功')
    return flask.redirect(flask.url_for('view_index.index'))


@view_account.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    from forms.sign_up import FormSignUp
    form = FormSignUp()
    if form.validate_on_submit():
        from models.user import User
        user = User(
            form.account.data,
            form.password.data,
            form.real_name.data,
            form.id_number.data,
            form.email.data,
            form.cellphone.data,
        )
        if user.new_user():
            flask.flash('注册成功')
            return flask.redirect(flask.url_for('view_index.index'))
        else:
            flask.flash('注册失败，账户名已被占用')
            return flask.redirect(flask.url_for('view_account.sign_up'))
    return flask.render_template('Account/sign_up.html', t='注册', form=form)


@view_account.route('/init_database')
def init_database():
    from start import db
    db.create_all()
    from models.user import User
    admin = User('sfg', '123456')
    admin.new_user()
    flask.flash('初始化数据库成功')
    return flask.redirect(flask.url_for('view_index.index'))
