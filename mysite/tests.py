from django.test import TestCase

from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from .views import index

class ServerPage(TestCase):

    def test_index_returns_correct_html(self):
        request = HttpRequest()

        response = index(request)
        html = response.content.decode('utf8')

        expected_content = render_to_string('mysite/index.html')
        self.assertEqual(html, expected_content)
