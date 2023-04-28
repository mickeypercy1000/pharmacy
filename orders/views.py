from django.shortcuts import render

from orders.models import PurchaseOrder

# Create your views here.
def purchaseOrderView(request):

    return render(request, "purchaseOrders.html")
