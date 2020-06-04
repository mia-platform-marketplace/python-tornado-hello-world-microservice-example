from tornado.testing import AsyncHTTPTestCase
import app
import json


class TestHelloApp(AsyncHTTPTestCase):
    def get_app(self):
        return app.make_app()

    def test_homepage(self):
        response = self.fetch('/hello')
        self.assertEqual(response.code, 200)
        doc = {'message': 'Hello World'}
        self.assertEqual(json.loads(response.body), doc)
