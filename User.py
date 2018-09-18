import flask_login


class User(flask_login.UserMixin):
    def get(self):
        return self
