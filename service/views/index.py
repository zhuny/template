from flask import Flask, Blueprint, render_template

from ._util import BaseView


class IndexView(BaseView):
    path = ["/", "/hello"]

    def get(self):
        return render_template("index.html")


def init(app: Flask):
    bp = Blueprint('index', __name__)
    IndexView.register(bp)

    app.register_blueprint(bp)

