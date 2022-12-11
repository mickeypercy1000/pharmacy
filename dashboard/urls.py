from dashboard.views import dashboard, sales
from stocks.views import addItemClass, deleteStock, expiry, stock
from django.urls import path

urlpatterns = [

    path('home/', dashboard, name = 'home'),
    path('sales/', sales, name = 'sales'),
    path('stock/', stock, name = 'stock'),
    path('expiry/', expiry, name = 'expiry'),
    path('add-item-class/', addItemClass, name = 'add-item-class'),
    path('delete-stock/<str:id>/', deleteStock, name = 'delete-stock'),

]