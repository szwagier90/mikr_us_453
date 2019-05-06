from django.shortcuts import render

from .models import Product

def home_page(request):
    product = Product()
    product.name = request.POST.get('product', '')
    product.save()

    return render(request, 'resources/home.html', {'product': product.name})
