# all products priced at $999 or less
from bangazonapi.models import Product
from django.shortcuts import render

def get_inexpensive_products(request):
    products = Product.objects.filter(price__lte=999).values('name', 'price', 'description')

    template = 'products/inexpensive_products.html'
     
    return render(request, template, context={'products': products})
