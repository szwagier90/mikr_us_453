from django.test import TestCase

from django.http import HttpRequest
from django.urls import resolve

from .views import index

class ResourcesPage(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_resources_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn('<title>Szwagier Mikrus Server</title>', response.content.decode('utf-8'))
        self.assertTrue(response.content.endswith(b'</html>'))
