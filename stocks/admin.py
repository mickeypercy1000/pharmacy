from django.contrib import admin

from stocks.models import Stock, DrugClass, ExpiryAlert

# Register your models here.
admin.site.register(Stock)
admin.site.register(DrugClass)
admin.site.register(ExpiryAlert)