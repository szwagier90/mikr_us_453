from django.test import TestCase

from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve

from .views import home_page

class ResourcesPage(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/resources/')
        self.assertEqual(found.func, home_page)

    def test_resources_page_returns_correct_html(self):
        response = self.client.get('/resources/')
        self.assertTemplateUsed(response, "resources/home.html")

    def test_can_save_POST_request(self):
        response = self.client.post('/resources/', data={'product': 'New Product'})
        self.assertIn('New Product', response.content.decode())
        self.assertTemplateUsed(response, "resources/home.html")
