from flask import Flask,render_template,redirect,request,url_for,flash,Blueprint,g
from App import App

app_view = Blueprint('app_view', __name__, template_folder='templates')
games = ["Flick Bird","Girls Foosball","Back to Back","Magic Invert"]

@app_view.route('/', methods=['GET','POST'])
def index():
    apps = []
    for game in games:
        app = App(game)
        apps.append(app)
    return render_template('/app_index.html',apps=apps)

@app_view.route('/flick_bird')
def flick_bird():
    return render_template('/app/flick_bird/flick_bird.html')

@app_view.route('/magic_invert')
def magic_invert():
    return render_template('/app/magic_invert/magic_invert.html')

@app_view.route('/walking_alien')
def walking_alien():
    return render_template('/app/walking_alien/walking_alien.html')

@app_view.route('/girls_foosball')
def girls_foosball():
    return render_template('/app/girls_foosball/girls_foosball.html')

@app_view.route('/back_to_back')
def back_to_back():
    return render_template('/app/back_to_back/back_to_back.html')