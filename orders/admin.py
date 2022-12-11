from django.contrib import admin

from orders.models import PurchaseOrder, receivedOrder

# Register your models here.
admin.site.register(PurchaseOrder)
admin.site.register(receivedOrder)