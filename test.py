import modelapp
from flask_wtf import FlaskForm
from wtforms import StringField


class A(FlaskForm):
    # 项目代码
    project_code = StringField(u'项目代号')

    def __init__(self):
        self.ooo = 0


def main():
    b = A()
    dic = dir(b)
    print(dic)
    lista  = vars(b)
    print(lista)


if __name__ == '__main__':
    main()
