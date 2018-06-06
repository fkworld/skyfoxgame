import datetime

from sqlalchemy import create_engine, Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from flask import url_for

# 一些长度常量
NAME_LENGTH = 64
URL_LENGTH = 128

# 初始化数据库连接
Base = declarative_base()
Engine = create_engine('sqlite:///database/app.db', encoding='utf-8')
Session = sessionmaker(bind=Engine)
session = Session()


class App(Base):
    """游戏APP主类
    """

    __tablename__ = 'apps'

    id = Column(Integer, primary_key=True)      # 项目id，自增
    project_code = Column(String(NAME_LENGTH))  # 项目代码
    # 中文介绍
    cname = Column(String(NAME_LENGTH))         # 中文名称
    ctext = Column(Text)                        # 中文文字介绍
    # 英文介绍
    ename = Column(String(NAME_LENGTH))         # 英文名称
    etext = Column(Text)                        # 英文文字介绍
    # 图标和宣传图的url（最高URL_LENGTH位）
    icon_url = Column(String(URL_LENGTH))       # icon的url
    show_url = Column(String(URL_LENGTH))       # show的url
    # 获取方式
    get_ios = Column(String(URL_LENGTH))        # appstore地址
    get_andriod = Column(String(URL_LENGTH))    # googleplay地址
    get_tap = Column(String(URL_LENGTH))        # taptap下载地址
    get_html = Column(String(URL_LENGTH))       # h5试玩地址
    get_wx = Column(String(URL_LENGTH))         # 微信小游戏地址
    # 上线相关
    online_date = Column(Date)                  # 上线时间
    # 排序方式
    sequence = Column(Integer, default=1)       # 次序，同级的随机排列，0为最高，越低越高

    def init_db(self):
        """初始化数据表
        """

        Base.metadata.create_all(Engine)

    def drop_db(self):
        """删除数据表
        """

        Base.metadata.drop_all(Engine)

    def add_app(self):
        """添加一个app到数据库中
        """

        session.add(self)
        session.commit()

    def delete_app(self):
        """删除一个游戏类app
        """
        session.delete(self)
        session.commit()

    def update_app(self):
        """更新一个游戏类app
        """
        session.commit()

    def search_all(self):
        """查询并返回所有的app

        Returns:
            list(App()) -- 全部App列表
        """

        result = session.query(App).all()
        return result

    def search_app_by_id(self, id):
        """根据id查询app
        Arguments:
            id {number} -- 待查询的id
        Returns:
            App() -- 查询结果
        """

        result = session.query(App).filter_by(id=id).one()
        return result

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
