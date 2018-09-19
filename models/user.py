import flask_login
from start import db


class User(db.Model, flask_login.UserMixin):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))
    real_name = db.Column(db.String(100))
    id_number = db.Column(db.String(100))
    email = db.Column(db.String(120))
    cellphone = db.Column(db.String(120))

    def __init__(self, account, password, real_name=None, id_number=None, email=None, cellphone=None):
        self.account = str(account)
        self.password = str(password)
        self.real_name = str(real_name)
        self.id_number = str(id_number)
        self.email = str(email)
        self.cellphone = str(cellphone)

    def check_user_account(self):
        # 检测user的account是否已经存在
        if User.query.filter_by(account=self.account).first() != None:
            return False
        else:
            return True

    def new_user(self):
        # 创建新user
        if self.check_user_account():
            db.session.add(self)
            db.session.commit()
            return True
        else:
            return False

    def check_password(self):
        # 检测密码是否正确
        user = User.query.filter_by(account=self.account).first()
        if user == None:
            return False
        if self.password != user.password:
            return False
        else:
            return user
