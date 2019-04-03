from django.shortcuts import render

from resources.models import Product

def home_page(request):
	all_products = Product.objects.all()
	return render(request, 'resources/home.html', {'all_products': all_products})
