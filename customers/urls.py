from django.urls import path
from customers.views import customers, deleteCustomer, updateCustomer

urlpatterns = [

    path('', customers, name = 'customers'),
    path('update-customer/<str:customer_id>/', updateCustomer, name = 'update-customer'),
    path('delete-customer/<str:customer_id>/', deleteCustomer, name = 'delete-customer'),

]