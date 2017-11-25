from flask import url_for
from start import db


class App(db.Model):

    __tablename__ = 'apps'
    id = db.Column(db.Integer, primary_key=True)    # id
    cname = db.Column(db.String(64))                # 中文名称
    ename = db.Column(db.String(64))                # 英文名称
    icon_url = db.Column(db.String(64))             # icon的url，因为量级比较小，所以在本地管理；等量级变大以后再说
    show_url = db.Column(db.String(64))             # show的url
    dappstore = db.Column(db.String(64))            # appstore下载地址
    dgoogle = db.Column(db.String(64))              # googleplay下载地址
    dtaptap = db.Column(db.String(64))              # taptap下载地址
    text = db.Column(db.Text)                       # 文字介绍

    # 添加app
    def add_app(self):
        db.session.add(self)
        db.session.commit()

    # 查询所有app
    def search_all(self):
        return self.query.all()

    # 获取icon或者show的filename
    def get_filename(self, icon_or_show):
        filename = []
        filename.append(self.ename.lower().replace(' ', '_'))
        filename.append(icon_or_show)
        icon_filename = '_'.join(filename)
        return icon_filename

    # 设置icon的url
    def set_icon_url(self):
        self.icon_url = "/static/app/" + self.get_filename('icon') + '.png'

    # 设置show的url
    def set_show_url(self):
        self.show_url = "/static/app/" + self.get_filename('show') + '.png'
