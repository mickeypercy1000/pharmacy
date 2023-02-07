from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ItemClass(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)



class Stock(models.Model):

    Status = (
        ('active', 'Active'),
        ('inactive', 'Inactive')
    )
    name = models.CharField(max_length=250)
    item_class = models.ForeignKey(ItemClass, on_delete = models.CASCADE, max_length=20, null = True, blank = True, default=None)
    maximum_quantity = models.IntegerField(default=0)
    reorder_quantity = models.IntegerField(default=0)
    quantity = models.IntegerField(null = True, blank = True, default=0)
    selling_price = models.DecimalField(max_digits = 10, decimal_places =2, default=0.00)
    cost_price = models.DecimalField(max_digits = 10, decimal_places =2, default=0.00)
    shelf_number = models.CharField(max_length=20, null = True, blank = True, default=None)
    expiry_date = models.DateField(null = True, blank = True)
    status = models.CharField(choices=Status, max_length=20, null = True, blank = True, default=None)
    deleted = models.BooleanField(default=False, null = False, blank = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return f"{self.name} {self.id}"

    class Meta:
        ordering = ('name',)


class ExpiryAlert(models.Model):
    expiry_alert = models.CharField(max_length = 30, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now = True, null = True, blank = True)
    created_by = models.ForeignKey(User, on_delete = models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.expiry_alert + ' month(s)'

    class Meta:
        ordering = ('-updated_at', 'created_at')



class StockAdjustment(models.Model):
    name = models.ForeignKey(Stock, on_delete = models.DO_NOTHING, related_name = 'stock_adjustments')
    current_quantity = models.ForeignKey(Stock, on_delete =models.DO_NOTHING, related_name = 'old_quantity')
    new_quantity = models.ForeignKey(Stock, on_delete =models.DO_NOTHING, related_name = 'new_quantity')
    reason = models.TextField()
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete = models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

