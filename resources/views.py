from django.shortcuts import render

def home_page(request):
    return render(request, 'resources/home.html', {'product': request.POST.get('product', '')})
