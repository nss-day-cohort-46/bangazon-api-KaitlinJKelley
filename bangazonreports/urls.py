from bangazonreports.views import (get_inexpensive_products, get_expensive_products, get_completed_orders, get_incomplete_orders)
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('inexpensive_products', get_inexpensive_products),
    path('expensive_products', get_expensive_products),
    path('completed_orders', get_completed_orders),
    path('incomplete_orders', get_incomplete_orders),
]
