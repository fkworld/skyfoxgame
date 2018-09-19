import flask_wtf
import wtforms


class FormSignUp(flask_wtf.FlaskForm):
    '''
    注册表单
    '''

    account = wtforms.StringField(
        label='账号：',
        validators=[
            wtforms.validators.DataRequired(message='账号不能为空'),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入账号',
        }
    )
    password = wtforms.PasswordField(
        label='密码',
        validators=[
            wtforms.validators.DataRequired(message='密码不能为空'),
        ],
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入密码',
        }
    )
    real_name = wtforms.StringField(
        label='真实姓名',
        render_kw={
            'class': 'form-control',
            'placeholder': '请填写真实姓名',
        }
    )
    id_number = wtforms.StringField(
        label='身份证号',
        render_kw={
            'class': 'form-control',
            'placeholder': '请填写身份证号',
        }
    )
    cellphone = wtforms.StringField(
        label='手机号',
        render_kw={
            'class': 'form-control',
        }
    )
    email = wtforms.StringField(
        label='电子邮箱',
        render_kw={
            'class': 'form-control',
        }
    )
    submit = wtforms.SubmitField(
        label='登录',
    )
