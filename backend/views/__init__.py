from flask import Flask
from flask_resty import Api


def init(app: Flask):
    api = Api(app, "/api/v1")

    from .index import init as index_init
    index_init(app, api)
