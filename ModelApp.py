from flask import url_for
from start import db


class App(db.Model):

    __tablename__ = 'apps'
    id = db.Column(db.Integer, primary_key=True)    # id
    cname = db.Column(db.String(64))                # 中文名称
    ename = db.Column(db.String(64))                # 英文名称
    # icon的url，因为量级比较小，所以在本地管理；等量级变大以后再说
    icon_url = db.Column(db.String(64))
    show_url = db.Column(db.String(64))             # show的url
    dios = db.Column(db.String(64))                 # ios下载地址
    dgoogle = db.Column(db.String(64))              # googleplay下载地址
    dtaptap = db.Column(db.String(64))              # taptap下载地址

    '''
    def __init__(self, name, icon_filename="icon.png", picture_filename="pic.png", txt_filename="txt.txt"):
        self.name = name
        url_name = self.name.lower().replace(" ", "_")
        from app_view import app_view
        self.url = url_for("app_view." + url_name)
        self.icon = url_for("static", filename="app/" + url_name + "/" + icon_filename)
        self.picture = url_for("static", filename="app/" + url_name + "/" + picture_filename)

        try:
            # 这里读取文件的路径需要删除第一个"/"字符
            file_url = url_for("static", filename="app/" + url_name + "/" + txt_filename).replace("/","",1)
            txt_file = open(file_url,"r")
            txts = txt_file.readlines()
            self.download_appstore = txts.pop(0)
            print(self.download_appstore.replace("\n",""))
            self.download_googleplay = txts.pop(0)
            self.download_taptap = txts.pop(0)
            self.text = txts
        finally:
            txt_file.close( )
            '''

    # 添加app
    def add_app(self):
        db.session.add(self)
        db.session.commit()

    # 查询所有app
    def search_all(self):
        return self.query.all()

    # 获取icon的filename
    def get_icon_filename(self):
        filename = []
        filename.append(self.ename.lower().replace(' ', '_'))
        filename.append('icon')
        icon_filename = '_'.join(filename)
        return icon_filename

    # 设置icon的url
    def set_icon_url(self):
        self.icon_url = "/static/app/" + self.get_icon_filename() + '.png'
        print(self.icon_url)
