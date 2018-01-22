from flask import Flask, render_template, redirect, request, url_for, flash, Blueprint, g

view_index = Blueprint('view_index', __name__, template_folder='templates')


@view_index.route('/', methods=['GET', 'POST'])
def index():
    """网站首页
    """
    # 由于首页还没有设计完成，所以这里临时做一个重定向
    return redirect(url_for("view_app.index"))


@view_index.route('/contact_us')
def contact_us():
    """联系我们
    """
    return render_template('contact_us.html')


@view_index.route('/privacy_policy')
def privacy_policy():
    """隐私政策
    """
    return render_template('privacy_policy.html')
