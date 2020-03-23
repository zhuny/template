from flask import Flask


def init(app: Flask):
    from .index import init as index_init
    index_init(app)


