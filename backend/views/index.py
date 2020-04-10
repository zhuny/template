from flask import Flask
from flask_resty import GenericModelView, Api


class IndexViewBase(GenericModelView):
    pass


class IndexListView(IndexViewBase):
    def get(self):
        return self.list()

    def post(self):
        return self.create()


class IndexView(IndexViewBase):
    def get(self, id):
        return self.retrieve(id)

    def patch(self, id):
        return self.update(id, partial=True)

    def delete(self, id):
        return self.destroy(id)


def init(app: Flask, api: Api):
    api.add_resource('/index', IndexView, IndexListView)

