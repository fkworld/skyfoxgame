from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import Required, Length, URL, Optional
from flask_wtf.file import FileField, FileRequired, FileAllowed


class AppForm(FlaskForm):
    projectcode = StringField(u"项目代码", validators=[Required(), Length(1, 64)])
    sequence = IntegerField(u"次序等级", validators=[Optional()])
    ename = StringField(u"英文名", validators=[Optional(), Length(1, 64)])
    cname = StringField(u"中文名", validators=[Optional(), Length(1, 64)])
    from start import appimages
    icon = FileField(u"图标", validators=[Optional(), FileAllowed(appimages, u"请选择图片")])
    show = FileField(u"宣传图", validators=[Optional(), FileAllowed(appimages, u"请选择图片")])
    dappstore = StringField(u"appstore下载地址", validators=[Optional(), URL(u"需要输入一个合理的URL")])
    dgoogle = StringField(u"googleplay下载地址", validators=[Optional(), URL()])
    dtaptap = StringField(u"taptap地址", validators=[Optional(), URL()])
    ctext = TextAreaField()
    etext = TextAreaField()

    submit = SubmitField(u"提交")

    def form_to_object(self, app):
        app.projectcode = self.projectcode.data
        app.sequence = self.sequence.data
        app.ename = self.ename.data
        app.cname = self.cname.data
        app.dappstore = self.dappstore.data
        app.dgoogle = self.dgoogle.data
        app.dtaptap = self.dtaptap.data
        app.ctext = self.ctext.data
        app.etext = self.etext.data

    def object_to_form(self, app):
        self.projectcode.data = app.projectcode
        self.sequence.data = app.sequence
        self.ename.data = app.ename
        self.cname.data = app.cname
        self.dappstore.data = app.dappstore
        self.dgoogle.data = app.dgoogle
        self.dtaptap.data = app.dtaptap
        self.ctext.data = app.ctext
        self.etext.data = app.etext

    # 保存icon和show文件
    def save_app_images(self, app):
        from start import appimages
        if self.icon.data is not None:
            icon = appimages.save(self.icon.data, name=app.get_filename('icon'))
            app.icon_url = appimages.url(icon)
        if self.show.data is not None:
            show = appimages.save(self.show.data, name=app.get_filename('show'))
            app.show_url = appimages.url(show)
