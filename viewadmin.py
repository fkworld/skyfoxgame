from flask import Flask, render_template, redirect, request, url_for, flash, Blueprint, g

view_admin = Blueprint('view_admin', __name__, template_folder='templates')


@view_admin.route('/')
def index():
    """管理员主页
    """
    from modelapp import App
    app = App()
    apps = app.search_all()
    app.order_by_sequence(apps)
    return render_template('/admin_index.html', apps=apps, title="开心吗")


@view_admin.route('/add_app', methods=['GET', 'POST'])
def add_app():
    """新建app页面
    """
    from formapp import AppForm
    from modelapp import App
    form = AppForm()
    app = App()
    if form.validate_on_submit():
        form.form_to_object(app)
        form.save_app_images(app)
        app.add_app()
        return redirect(url_for('view_admin.index'))
    return render_template('edit_app.html', form=form, title="新建APP")


@view_admin.route('/edit_app/<app_id>', methods=['GET', 'POST'])
def edit_app(app_id):
    """根据id进入编辑app页面
    """
    from formapp import AppForm
    from modelapp import App
    app = App()
    form = AppForm()
    app = app.search_by_id(app_id)
    if form.validate_on_submit():
        form.form_to_object(app)
        form.save_app_images(app)
        app.update_app()
        return redirect(url_for('view_admin.index'))
    form.object_to_form(app)  # 这行应该改。逻辑上应该传入app的内容，然后将app的内容填入表单中。以后再改
    return render_template('edit_app.html', form=form, app=app, title='修改APP')


@view_admin.route('/delete_app/<app_id>', methods=['GET', 'POST'])
def delete_app(app_id):
    """根据id删除app
    """
    from modelapp import App
    app = App()
    app = app.search_by_id(app_id)
    app.delete_app()
    return redirect(url_for('view_admin.index'))
