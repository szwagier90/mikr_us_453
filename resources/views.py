from django.shortcuts import redirect, render

from .models import Product

def home_page(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST.get('product', ''),
            quantity=request.POST.get('quantity', ''),
            pieces=request.POST.get('pieces', 1),
        )
        return redirect('/resources/')

    products = Product.objects.all()

    return render(request, 'resources/home.html', {
        'products': products,
    })
