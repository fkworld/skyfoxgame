from flask import Flask,render_template,redirect,request,url_for,flash,Blueprint,g

app_view = Blueprint('app_view', __name__, template_folder='templates')

@app_view.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

@app_view.route('/flick_bird')
def flick_bird():
    return render_template('app_flick_bird.html')