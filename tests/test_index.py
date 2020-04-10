import unittest

from main import app


class IndexTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

