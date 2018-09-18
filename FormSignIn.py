import flask_wtf
import wtforms


class FormSignIn(flask_wtf.FlaskForm):
    account = wtforms.StringField(
        label='账号：',
        validators=[
            wtforms.validators.InputRequired(message='11111111'),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入账号',
        }
    )
    password = wtforms.PasswordField(
        label='密码',
        validators=[
            wtforms.validators.DataRequired(),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入密码',
        }
    )
    submit = wtforms.SubmitField(
        label='登录',
    )
