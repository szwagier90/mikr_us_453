from django.test import TestCase

from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve

from .views import index

class ResourcesPage(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_resources_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)

        expected_content = render_to_string('mysite/index.html')
        self.assertEqual(response.content.decode(), expected_content)
