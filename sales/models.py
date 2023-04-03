from django.db import models

from stocks.models import Stock
from django.contrib.auth.models import User
import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Sales(models.Model):

    STATUS = (
        ('Cash', 'cash'),
        ('Credit', 'credit'),
    )
    id = models.CharField(
        _("id"),
        max_length=50,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
    )

    item_name = models.ManyToManyField(Stock)
    sales_person = models.ForeignKey(User, on_delete = models.DO_NOTHING, related_name = "Sales_Person")
    quantity = models.IntegerField()
    amount = models.DecimalField(decimal_places = 2, max_digits =10)
    status = models.CharField(choices = STATUS, max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.sales_person}"

    class Meta:
        ordering = ('-created_at',)