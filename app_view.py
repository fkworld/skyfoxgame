from flask import Flask,render_template,redirect,request,url_for,flash,Blueprint,g

app_view = Blueprint('app_view', __name__, template_folder='templates')

@app_view.route('/', methods=['GET','POST'])
def index():
    return render_template('/app/app_index.html')

@app_view.route('/flick_bird')
def flick_bird():
    return render_template('/app/flick_bird/flick_bird.html')

@app_view.route('/magic_invert')
def magic_invert():
    return render_template('/app/magic_invert/magic_invert.html')

@app_view.route('/walking_alien')
def walking_alien():
    return render_template('/app/walking_alien/walking_alien.html')