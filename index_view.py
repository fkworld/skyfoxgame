from flask import Flask,render_template,redirect,request,url_for,flash,Blueprint,g

index_view = Blueprint('index_view', __name__, template_folder='templates')

@index_view.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')