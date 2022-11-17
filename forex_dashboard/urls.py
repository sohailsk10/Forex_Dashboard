from django.contrib import admin
from django.urls import path, include
from forex_app import views
import forex.views as BT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard),
    path('logout', views.logout, name='logout'),

    path('get_data', views.get_data, name= "get_data"),
    path('get_currency', views.get_currency, name= "get_currency"),

    path('predict/', BT.predict),
    path('get-model/', BT.get_model),
    path('forex/', include('forex.urls')),
    path('index/', BT.index, name="index"),
    path('index/<currency>/', BT.currency, name="currency"),
    path('index/<currency>/<interval>/', BT.interval, name="interval"),
    path('report/', BT.report, name="report"),
    path('report-status/<report_status_id>/', BT.report_status, name="report-status"),
]
