import flask_wtf
import wtforms


class FormSignIn(flask_wtf.FlaskForm):
    account = wtforms.StringField(
        label='账号：',
        validators=[
            wtforms.validators.DataRequired(message='账号不能为空'),
        ],
        widget=wtforms.widgets.TextInput(),
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入账号',
            'required': '',
            'autofocus': ''
        }
    )
    password = wtforms.PasswordField(
        label='密码',
        validators=[
            wtforms.validators.DataRequired(message='密码不能为空'),
        ],
        widget=wtforms.widgets.PasswordInput(),
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入密码',
            'required': '',
            'autofocus': ''
        }
    )
    submit = wtforms.SubmitField(
        label='登录',
    )
