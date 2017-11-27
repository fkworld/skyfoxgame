from flask import Flask, render_template, redirect, request, url_for, flash, Blueprint, g

admin_view = Blueprint('admin_view', __name__, template_folder='templates')


@admin_view.route('/')
def index():
    from ModelApp import App
    app = App()
    apps = app.search_all()
    app.order_by_sequence(apps)
    return render_template('/admin_index.html', apps=apps, title="开心吗")


@admin_view.route('/add_app', methods=['GET', 'POST'])
def add_app():
    from FormApp import AppForm
    from ModelApp import App
    form = AppForm()
    app = App()
    if form.validate_on_submit():
        print("gggg")
        form.form_to_object(app)
        app.set_icon_url()
        app.set_show_url()
        app.add_app()
        return redirect(url_for('admin_view.index'))
    return render_template('edit_app.html', form=form, title="新建APP")


@admin_view.route('/edit_app/<app_id>', methods=['GET', 'POST'])
def edit_app(app_id):
    from FormApp import AppForm
    from ModelApp import App
    app = App()
    form = AppForm()
    app = app.search_by_id(app_id)
    if form.validate_on_submit():
        form.form_to_object(app)
        app.update_app()
        return redirect(url_for('admin_view.index'))
    form.object_to_form(app)
    return render_template('edit_app.html', form=form, title='修改APP')


@admin_view.route('/delete_app/<app_id>', methods=['GET', 'POST'])
def delete_app(app_id):
    from ModelApp import App
    app = App()
    app = app.search_by_id(app_id)
    app.delete_app()
    return redirect(url_for('admin_view.index'))

