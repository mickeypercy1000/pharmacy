from django.contrib import admin

from customers.models import Customer
from suppliers.models import Supplier

from .models import Stock, ItemClass, ExpiryAlert

# Register your models here.
admin.site.register(Stock)
admin.site.register(ItemClass)
admin.site.register(ExpiryAlert)
