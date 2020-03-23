from flask import Flask, Blueprint

from ._util import BaseView


class IndexView(BaseView):
    path = ["/", "/hello"]

    def get(self):
        return "Hello World!"


def init(app: Flask):
    bp = Blueprint('index', __name__)
    IndexView.register(bp)

    app.register_blueprint(bp)

