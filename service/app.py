from flask import Flask


def create_app():
    app = Flask(__name__)

    from .views import init as views_init
    views_init(app)

    from .user import init as user_init
    user_init(app)

    return app

