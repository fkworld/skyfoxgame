from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, DateField
from wtforms.validators import DataRequired, Length


class AppForm(FlaskForm):
    """app编辑表单
    """
    # 项目代码
    project_code = StringField(u'项目代号')
    # 中文介绍
    cname = StringField(u'中文名称')
    ctext = TextAreaField(u'中文介绍')
    # 英文介绍
    ename = StringField(u'英文名称')
    etext = TextAreaField(u'英文介绍')
    # 图标和宣传图的url
    icon_url = StringField(u'图标URL')
    show_url = StringField(u'宣传图URL')
    # 获取方式
    get_ios = StringField(u'APPSTORE获取地址')
    get_andriod = StringField(u'GOOGLEPLAY获取地址')
    get_tap = StringField(u'TAPTAP获取地址')
    get_html = StringField(u'HTML5获取地址')
    get_wx = StringField(u'微信小游戏获取地址')
    # 上线时间
    online_date = StringField(u'上线时间')
    # 排序方式
    sequence = StringField(u'次序等级')
    submit = SubmitField(u'提交')

    def form_to_object(self, app):
        """表单内容写入app类
        """
        app.project_code = self.project_code.data
        app.cname = self.cname.data
        app.ctext = self.ctext.data
        app.ename = self.ename.data
        app.etext = self.etext.data
        app.icon_url = self.icon_url.data
        app.show_url = self.show_url.data
        app.get_ios = self.get_ios.data
        app.get_andriod = self.get_andriod.data
        app.get_tap = self.get_tap.data
        app.get_html = self.get_html.data
        app.get_wx = self.get_wx.data
        app.sequence = self.sequence.data
        pass

    def object_to_form(self, app):
        """app内容写入表单
        """
        pass

    def save_app_images(self, app):
        """保存app的icon和show的图片
        """
        pass
