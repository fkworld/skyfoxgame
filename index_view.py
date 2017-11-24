from flask import Flask,render_template,redirect,request,url_for,flash,Blueprint,g

index_view = Blueprint('index_view', __name__, template_folder='templates')

@index_view.route('/', methods=['GET','POST'])
def index():
    return redirect(url_for("app_view.index"))

@index_view.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')

@index_view.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@index_view.route('/ilovefangchunpin', methods=['GET','POST'])
def test():
    from FormApp import AppForm
    form = AppForm()
    from ModelApp import App
    app = App()
    if form.validate_on_submit():
        form.form_to_object(app)
        app.set_icon_url()
        app.add_app()
        return redirect(url_for('index_view.index'))
    return render_template('edit_app.html',form=form,title="新建APP")
        