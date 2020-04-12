import unittest

from main import app


class IndexTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_restful(self):
        resp1 = self.client.get("/index")
        resp2 = self.client.get("/index/123")

