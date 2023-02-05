from django.contrib import admin

from stocks.models import Stock, ItemClass, ExpiryAlert

# Register your models here.
admin.site.register(Stock)
admin.site.register(ItemClass)
admin.site.register(ExpiryAlert)