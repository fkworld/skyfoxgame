from flask import Flask,render_template,redirect,request,url_for,flash,Blueprint,g

app_view = Blueprint('app_view', __name__, template_folder='templates')
games = ["Flick Bird","Girls Foosball","Back to Back","Magic Invert"]

@app_view.route('/', methods=['GET','POST'])
def index():
    from ModelApp import App
    app = App()
    apps = app.search_all()
    return render_template('/app_index.html',apps=apps)