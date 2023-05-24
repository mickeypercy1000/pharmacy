from django.urls import path
from sales.views import allSales


urlpatterns = [
    path('', allSales, name = 'sales'),
]