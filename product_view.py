from flask import Flask,render_template,redirect,request,url_for,flash,Blueprint,g

product_view = Blueprint('product_view', __name__, template_folder='templates')

@product_view.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')