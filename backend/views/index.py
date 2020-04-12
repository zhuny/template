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
    def get(self, rid):
        return self.retrieve(rid)

    def patch(self, rid):
        return self.update(rid, partial=True)

    def delete(self, rid):
        return self.destroy(rid)


def init(app: Flask, api: Api):
    api.add_resource('/index', IndexView, IndexListView, id_rule='<rid>')

