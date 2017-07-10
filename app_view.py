from flask import Flask,render_template,redirect,request,url_for,flash,Blueprint,g

app_view = Blueprint('app_view', __name__, template_folder='templates')

@app_view.route('/', methods=['GET','POST'])
def index():
    return render_template('app_index.html')

@app_view.route('/flick_bird')
def flick_bird():
    return render_template('app_flick_bird.html')

@app_view.route('/walking_aliens')
def walking_aliens():
    return render_template('app_walking_aliens.html')

@app_view.route('/magic_invert')
def magic_invert():
    return render_template('app_magic_invert.html')