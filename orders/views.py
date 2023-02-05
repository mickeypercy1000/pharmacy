from django.shortcuts import render

from orders.models import PurchaseOrder

# Create your views here.
def purchaseOrder(request):

    return render(request, "purchaseOrders.html")
