from flask import url_for
from start import db


class App(db.Model):
    """游戏类app主类
    """

    __tablename__ = 'apps'
    id = db.Column(db.Integer, primary_key=True)    # 项目id
    projectcode = db.Column(db.String(64))          # 项目代码
    cname = db.Column(db.String(64))                # 中文名称
    ename = db.Column(db.String(64))                # 英文名称
    icon_url = db.Column(db.String(64))             # icon的url
    show_url = db.Column(db.String(64))             # show的url
    dappstore = db.Column(db.String(64))            # appstore下载地址
    dgoogle = db.Column(db.String(64))              # googleplay下载地址
    dtaptap = db.Column(db.String(64))              # taptap下载地址
    ctext = db.Column(db.Text)                      # 中文文字介绍
    etext = db.Column(db.Text)                      # 英文文字介绍
    sequence = db.Column(db.Integer, default=0)     # 次序，同级的随机排列，0为最高

    def add_app(self):
        """添加一个游戏类app
        """
        db.session.add(self)
        db.session.commit()

    def delete_app(self):
        """删除一个游戏类app
        """
        db.session.delete(self)
        db.session.commit()

    def update_app(self):
        """更新一个游戏类app
        """
        db.session.commit()

    def search_all(self):
        """查询数据库类所有的游戏类app
        """
        return self.query.all()

    def order_by_sequence(self, apps):
        """按照sequence的等级排序
        """
        try:
            # 由于生产环境数据库中可能没有sequence项，所以这里用try-except作封装
            apps.sort(key=lambda x: x.sequence)
        except:
            pass

    def search_by_id(self, id):
        """根据app的id查询app
        返回查询结果
        """
        return self.query.filter_by(id=id).first_or_404()

    def get_filename(self, icon_or_show):
        """根据app的projectcode生成filename前缀
        返回filename前缀字符串
        """
        filename = []
        filename.append(str(self.id))
        filename.append(self.projectcode.lower().replace(' ', '_'))
        filename.append(icon_or_show)
        return_filename = '_'.join(filename)
        # 以'.'为结尾，保存的时候会自动填充文件后缀
        return_filename += '.'
        return return_filename
