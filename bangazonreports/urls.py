from bangazonreports.views import get_inexpensive_products
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('inexpensive_products', get_inexpensive_products)
]
