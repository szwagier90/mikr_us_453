from django.shortcuts import render

from .models import Product

def home_page(request):
    if request.method == 'POST':
        new_product_name = request.POST.get('product', '')
        Product.objects.create(name=new_product_name)
    else:
        new_product_name = ''

    return render(request, 'resources/home.html', {
        'product': new_product_name
    })
