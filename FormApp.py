from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required,Length

class AppForm(FlaskForm):
    cname = StringField("中文名", validators=[Required(),Length(1,64)])
    ename = StringField("英文名", validators=[Required(),Length(1,64)])
    dappstore = StringField("ios下载地址", validators=[Length(1,64)])
    dgoogle = StringField("googleplay下载地址", validators=[Length(1,64)])
    dtaptap = StringField("taptap地址", validators=[Length(1,64)])
    text = TextAreaField()

    submit = SubmitField("提交")

    def form_to_object(self, app):
        app.cname = self.cname.data
        app.ename = self.ename.data
        app.dappstore = self.dappstore.data
        app.dgoogle = self.dgoogle.data
        app.dtaptap = self.dtaptap.data
        app.text = self.text.data
