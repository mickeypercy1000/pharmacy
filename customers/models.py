from django.db import models

# Create your models here.
    
class Customer(models.Model):

    businessOptions = (
        ('ind','Individual'),
        ('bus','Business')
    )
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    businessName = models.CharField(max_length=100, unique=True, null=True, blank=True)
    businessType = models.CharField(max_length=20, choices = businessOptions)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __string__(self):
        return self.businessName

    class Meta:
        ordering = ('businessName',)