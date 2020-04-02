import os

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


def create_app():
    app = Flask(__name__)

    from .views import init as views_init
    views_init(app)

    from .user import init as user_init
    user_init(app)

    from service.assets import init as assets_init
    assets_init(app)

    app.secret_key = os.urandom(16)
    toolbar = DebugToolbarExtension(app)

    return app

