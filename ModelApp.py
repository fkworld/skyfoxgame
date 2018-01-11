from flask import url_for
from start import db


class App(db.Model):

    __tablename__ = 'apps'
    id = db.Column(db.Integer, primary_key=True)    # id
    projectcode = db.Column(db.String(64))          # 项目代码
    cname = db.Column(db.String(64))                # 中文名称
    ename = db.Column(db.String(64))                # 英文名称
    icon_url = db.Column(db.String(64))             # icon的url，因为量级比较小，所以在本地管理；等量级变大以后再说
    show_url = db.Column(db.String(64))             # show的url
    dappstore = db.Column(db.String(64))            # appstore下载地址
    dgoogle = db.Column(db.String(64))              # googleplay下载地址
    dtaptap = db.Column(db.String(64))              # taptap下载地址
    ctext = db.Column(db.Text)                      # 中文文字介绍
    etext = db.Column(db.Text)                      # 英文文字介绍
    sequence = db.Column(db.Integer, default=0)     # 次序，同级的随机排列，0为最高

    # 添加app
    def add_app(self):
        db.session.add(self)
        db.session.commit()

    # 删除app
    def delete_app(self):
        db.session.delete(self)
        db.session.commit()
    
    # 更新app
    def update_app(self):
        db.session.commit()
        
    # 查询所有app
    def search_all(self):
        return self.query.all()

    # 按照sequence的等级排序
    def order_by_sequence(self, apps):
        # 由于生产环境中可能没有sequence项，所以这里用try-except作封装
        try:
            apps.sort(key=lambda x:x.sequence)
        except:
            pass

    # 根据id查询app
    def search_by_id(self,id):
        return self.query.filter_by(id=id).first_or_404()

    # 根据app的projectcode生成icon和show的filename
    def get_filename(self, icon_or_show):
        filename = []
        filename.append(str(self.id))
        filename.append(self.projectcode.lower().replace(' ', '_'))
        filename.append(icon_or_show)
        return_filename = '_'.join(filename)
        # 以'.'为结尾，保存的时候会自动填充
        return_filename += '.'
        return return_filename

    # 设置icon的url
    '''
    def set_icon_url(self):
        self.icon_url = "/static/app/" + self.get_filename('icon') + '.png'
        '''

    # 设置show的url
    '''
    def set_show_url(self):
        self.show_url = "/static/app/" + self.get_filename('show') + '.png'
        '''
