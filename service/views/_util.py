from typing import Union

from flask import Flask, Blueprint
from flask.views import MethodView


class BaseView(MethodView):
    path = None

    @classmethod
    def _iter_path(cls):
        if cls.path is None:
            raise ValueError("Path is needed")
        elif isinstance(cls.path, str):
            yield cls.path
        elif isinstance(cls.path, list):
            yield from cls.path
        else:
            raise ValueError("Unknown Path Type")

    @classmethod
    def register(cls, app: Union[Flask, Blueprint]):
        view_func = cls.as_view(cls.__name__)
        for path in cls._iter_path():
            app.add_url_rule(path, view_func=view_func)

