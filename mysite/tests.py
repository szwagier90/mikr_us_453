from django.test import TestCase

from django.urls import resolve
from django.template.loader import render_to_string

from .views import index

class ServerPage(TestCase):

    def test_index_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, "mysite/index.html")
