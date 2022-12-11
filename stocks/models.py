from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DrugClass(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)



class Stock(models.Model):
    status = (
        ('Active','active'),
        ('Inactive','inactive'),
    )
    name = models.CharField(max_length=20)
    item_class = models.ForeignKey(DrugClass, on_delete = models.CASCADE, max_length=20, null = True, blank = True, default=None)
    maximum_quantity = models.IntegerField(null = True, blank = True, default=None)
    reorder_quantity = models.IntegerField(null = True, blank = True, default=None)
    shelf_number = models.CharField(max_length=20, null = True, blank = True, default=None)
    expiry_date = models.DateField(null = True, blank = True)
    status = models.CharField(choices = status, max_length=20, null = True, blank = True, default=None)
    deleted = models.BooleanField(default=False, null = False, blank = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete = models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class ExpiryAlert(models.Model):
    expiry_alert = models.CharField(max_length = 30, null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True, null = True, blank = True)
    updated_at = models.DateTimeField(auto_now = True, null = True, blank = True)
    created_by = models.ForeignKey(User, on_delete = models.SET_NULL, blank=True, null=True)

