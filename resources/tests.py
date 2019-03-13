from django.test import TestCase
from django.http import HttpRequest

from resources.views import home_page

class ResourcesPage(TestCase):
    def test_resources_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn('<title>Produkty</title>', response.content.decode('utf-8'))
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertTrue(response.content.strip().endswith(b'</html>'))
