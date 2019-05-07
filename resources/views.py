from django.shortcuts import redirect, render

from .models import Product

def home_page(request):
    if request.method == 'POST':
        Product.objects.create(name=request.POST.get('product', ''))
        return redirect('/resources/')

    products = Product.objects.all()

    return render(request, 'resources/home.html', {
        'products': products,
    })
