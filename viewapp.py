from flask import Flask, render_template, redirect, request, url_for, flash, Blueprint, g

view_app = Blueprint('view_app', __name__, template_folder='templates')


@view_app.route('/', methods=['GET', 'POST'])
def index():
    from modelapp import App
    app = App()
    apps = app.search_all()
    app.order_by_sequence(apps)
    return render_template('/app_index.html', apps=apps)
