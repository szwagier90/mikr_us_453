from django.test import TestCase

from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve

from .models import Product

from .views import home_page

class ResourcesPage(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/resources/')
        self.assertEqual(found.func, home_page)

    def test_resources_page_returns_correct_html(self):
        response = self.client.get('/resources/')
        self.assertTemplateUsed(response, "resources/home.html")

    def test_can_save_POST_request(self):
        self.client.post('/resources/', data={'product': 'New Product'})

        self.assertEqual(1, Product.objects.count())
        new_product = Product.objects.first()
        self.assertEqual("New Product", new_product.name)

    def test_redirect_after_POST(self):
        response = self.client.post('/resources/', data={'product': 'New Product'})
        self.assertEqual(302, response.status_code)
        self.assertEqual('/resources/', response['location'])

    def test_save_product_only_when_post(self):
        self.client.get('/resources/')
        self.assertEqual(0, Product.objects.count())

    def test_show_all_products(self):
        Product.objects.create(name='Pomidor')
        Product.objects.create(name='Chleb')

        response = self.client.get('/resources/')

        self.assertIn('Pomidor', response.content.decode())
        self.assertIn('Chleb', response.content.decode())


class ProductModelTest(TestCase):
    def test_saving_and_retrieving_products(self):
        first_product = Product()
        first_product.name = 'Banan'
        first_product.save()

        second_product = Product()
        second_product.name = 'Kiwi'
        second_product.save()

        saved_products = Product.objects.all()
        self.assertEqual(2, saved_products.count())

        self.assertEqual('Banan', saved_products[0].name)
        self.assertEqual('Kiwi', saved_products[1].name)
