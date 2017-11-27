from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required,Length,URL,Optional

class AppForm(FlaskForm):
    projectcode = StringField(u"项目代码", validators=[Required(),Length(1,64)])
    ename = StringField(u"英文名", validators=[Optional(),Length(1,64)])
    cname = StringField(u"中文名", validators=[Optional(),Length(1,64)])
    dappstore = StringField(u"appstore下载地址", validators=[Optional(),URL(u"需要输入一个合理的URL")])
    dgoogle = StringField(u"googleplay下载地址", validators=[Optional(),URL()])
    dtaptap = StringField(u"taptap地址", validators=[Optional(),URL()])
    ctext = TextAreaField()
    etext = TextAreaField()

    submit = SubmitField(u"提交")

    def form_to_object(self, app):
        app.projectcode = self.projectcode.data
        app.ename = self.ename.data
        app.cname = self.cname.data
        app.dappstore = self.dappstore.data
        app.dgoogle = self.dgoogle.data
        app.dtaptap = self.dtaptap.data
        app.ctext = self.ctext.data
        app.etext = self.etext.data

    def object_to_form(self,app):
        self.projectcode.data = app.projectcode
        self.ename.data = app.ename
        self.cname.data = app.cname
        self.dappstore.data = app.dappstore
        self.dgoogle.data = app.dgoogle
        self.dtaptap.data = app.dtaptap
        self.ctext.data = app.ctext
        self.etext.data = app.etext