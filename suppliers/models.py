from django.db import models
from django.contrib.auth.models import User
import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Supplier(models.Model):
    id = models.CharField(
        _("id"),
        max_length=50,
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.created_at}"

    class Meta:
        ordering = ('name',)
