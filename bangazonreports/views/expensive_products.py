# all products priced at $1000 or more
from bangazonapi.models import Product
from django.shortcuts import render

def get_expensive_products(request):
    products = Product.objects.filter(price__gt=999).values('name', 'price', 'description')

    template = 'products/expensive_products.html'
     
    return render(request, template, context={'products': products})