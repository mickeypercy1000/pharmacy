from django.db import models
from stock.models import Stock
from suppliers.models import *
from django.contrib.auth.models import User
from suppliers.models import Supplier
import uuid
from django.utils.translation import gettext_lazy as _


# Create your models here. 

# Create your models here.
class PurchaseOrder(models.Model):
    id = models.CharField(
        _("id"),
        max_length=50,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
    )

    orderType = (
        ('cash','Cash'),
        ('credit','Credit')
    )
    item = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING)
    person_requesting = models.OneToOneField(User, on_delete = models.SET_NULL, max_length=100, unique=True, null=True, blank=True)
    order_type = models.CharField(max_length=20, choices = orderType, default = orderType[0])
    note = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item, self.amount, self.person_requesting, self.order_type


class receivedOrder(models.Model):
    orderStatus = (
        ('pending','Pending'),
        ('received','Received'),
        ('cancelled','Cancelled'),
    )
    id = models.CharField(
        _("id"),
        max_length=50,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
    )
    order = models.ForeignKey(PurchaseOrder, on_delete=models.DO_NOTHING, related_name="received_order")
    item = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    person_receiving = models.OneToOneField(User, on_delete = models.SET_NULL, max_length=100, unique=True, null=True, blank=True)
    status = models.CharField(max_length=20, choices = orderStatus, default = orderStatus[0])
    note = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item, self.amount, self.orderStatus, self.person_receiving