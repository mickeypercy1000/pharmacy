from django.urls import path
from suppliers.views import suppliers, updateSupplier, deleteSupplier

urlpatterns = [

    path('', suppliers, name = 'suppliers'),
    path('update-supplier/<str:supplier_id>/', updateSupplier, name = 'update-supplier'),
    path('delete-supplier/<str:supplier_id>/', deleteSupplier, name = 'delete-supplier')

]