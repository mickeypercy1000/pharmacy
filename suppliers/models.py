from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name, self.phone