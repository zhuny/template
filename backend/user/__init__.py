from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    pass


def init(app: Flask):
    login_manager.init_app(app)

