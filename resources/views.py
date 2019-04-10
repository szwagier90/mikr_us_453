from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from resources.models import Product

@login_required
def home_page(request):
	all_products = Product.objects.all()
	return render(request, 'resources/home.html', {'all_products': all_products})
