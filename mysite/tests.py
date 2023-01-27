from django.test import TestCase

from django.urls import resolve
from django.http import HttpRequest

from .views import index

class ServerPage(TestCase):

    def test_index_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Szwagier Mikrus Server</title>', html)
        self.assertTrue(html.endswith('</html>'))
