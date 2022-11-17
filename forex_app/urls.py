from django.urls import path, include
from .views import *
from django.contrib import admin
from rest_framework import routers



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard),
    path('logout', logout),
]


