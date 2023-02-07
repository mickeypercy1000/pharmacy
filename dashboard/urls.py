from dashboard.views import dashboard, sales
from orders.views import purchaseOrder
from stocks.views import addStock, deleteStock, stock, itemAdjustment, updateStock
from django.urls import path

from suppliers.views import suppliers, updateSupplier, deleteSupplier
from customers.views import customers, deleteCustomer, updateCustomer

urlpatterns = [

    path('home/', dashboard, name = 'home'),
    path('sales/', sales, name = 'sales'),

    path('stock/', stock, name = 'stock'),
    path('add-stock/', addStock, name = 'add-stock'),
    path('update-stock/<str:stock_id>/', updateStock, name = 'update-stock'),
    path('delete-stock/<str:stock_id>/', deleteStock, name = 'delete-stock'),

    path('suppliers/', suppliers, name = 'suppliers'),
    path('update-supplier/<str:supplier_id>/', updateSupplier, name = 'update-supplier'),
    path('delete-supplier/<str:supplier_id>/', deleteSupplier, name = 'delete-supplier'),

    path('customers/', customers, name = 'customers'),
    path('update-customer/<str:customer_id>/', updateCustomer, name = 'update-customer'),
    path('delete-customer/<str:customer_id>/', deleteCustomer, name = 'delete-customer'),

    path('purchase-order/', purchaseOrder, name = 'purchase-order/'),
    path('item-adjustment/', itemAdjustment, name = 'item-adjustment'),
    # path('expiry/', expiry, name = 'expiry'),
    # path('add-item-class/', addItemClass, name = 'add-item-class'),
    # path('delete-stock/<str:id>/', deleteStock, name = 'delete-stock'),

]