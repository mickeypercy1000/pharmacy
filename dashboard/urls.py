from dashboard.views import dashboard, sales
from stocks.views import stock
from django.urls import path

from suppliers.views import suppliers, updateSupplier, deleteSupplier
from customers.views import customers, updateCustomer

urlpatterns = [

    path('home/', dashboard, name = 'home'),
    path('sales/', sales, name = 'sales'),
    path('stock/', stock, name = 'stock'),
    path('suppliers/', suppliers, name = 'suppliers'),
    path('update-supplier/<str:supplier_id>/', updateSupplier, name = 'update-supplier'),
    path('delete-supplier/<str:supplier_id>/', deleteSupplier, name = 'delete-supplier'),
    path('customers/', customers, name = 'customers'),
    path('update-customer/<str:customer_id>/', updateCustomer, name = 'update-customer'),
    # path('expiry/', expiry, name = 'expiry'),
    # path('add-item-class/', addItemClass, name = 'add-item-class'),
    # path('delete-stock/<str:id>/', deleteStock, name = 'delete-stock'),

]