from .views import *
from django.conf.urls import url
from rest_framework import routers
from django.urls import path, include


router = routers.DefaultRouter()
router.register('get-currency', CurrencyViewSet)
router.register('get-interval', IntervalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]