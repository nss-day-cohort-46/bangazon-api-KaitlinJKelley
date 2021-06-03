from django.conf.urls import url, include
from django.urls import path
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from bangazonapi.models import *
from bangazonapi.views import *

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('^', include(router.urls))
]
