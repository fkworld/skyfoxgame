from flask import Flask, render_template, redirect, request, url_for, flash, Blueprint, g

admin_view = Blueprint('admin_view', __name__, template_folder='templates')


@admin_view.route('/')
def index():
    from modelapp import App
    app = App()
    apps = app.search_all()
    app.order_by_sequence(apps)
    return render_template('/admin_index.html', apps=apps, title="开心吗")


@admin_view.route('/add_app', methods=['GET', 'POST'])
def add_app():
    from FormApp import AppForm
    from modelapp import App
    form = AppForm()
    app = App()
    if form.validate_on_submit():
        form.form_to_object(app)
        form.save_app_images(app)
        app.add_app()
        return redirect(url_for('admin_view.index'))
    return render_template('edit_app.html', form=form, title="新建APP")


@admin_view.route('/edit_app/<app_id>', methods=['GET', 'POST'])
def edit_app(app_id):
    from FormApp import AppForm
    from modelapp import App
    app = App()
    form = AppForm()
    app = app.search_by_id(app_id)
    if form.validate_on_submit():
        form.form_to_object(app)
        form.save_app_images(app)
        app.update_app()
        return redirect(url_for('admin_view.index'))
    form.object_to_form(app) # 这行应该改。逻辑上应该传入app的内容，然后将app的内容填入表单中。以后再改
    return render_template('edit_app.html', form=form, app=app, title='修改APP')


@admin_view.route('/delete_app/<app_id>', methods=['GET', 'POST'])
def delete_app(app_id):
    from modelapp import App
    app = App()
    app = app.search_by_id(app_id)
    app.delete_app()
    return redirect(url_for('admin_view.index'))

