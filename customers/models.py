from django.db import models
from django.contrib.auth.models import User


# Create your models here. 
class Customer(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    id_card_number = models.CharField(max_length=100, unique=True)
    # id_card = models.FileField()
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __string__(self):
        return self.name

    class Meta:
        ordering = ('name',)