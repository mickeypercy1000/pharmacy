from django.shortcuts import render

from orders.models import PurchaseOrder

# Create your views here.
def purchase(request):
    purchase = PurchaseOrder.objects.filter(id = '1')
    if purchase is not None:
        purchase.delete()
    