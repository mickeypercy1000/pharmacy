from django.urls import include, path

from orders.views import purchaseOrderView


urlpatterns = [
    # path('', purchase, name = 'home'),
    path('purchase-order/', purchaseOrderView, name = 'purchase-order/'),

]
