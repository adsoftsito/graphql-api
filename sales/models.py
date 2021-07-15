from django.db import models
from django.conf import settings


# Create your models here.
class Sale(models.Model):
    subtotal = models.FloatField(default=0)
    iva = models.FloatField(default=0)
    total = models.FloatField(default=0)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


# Product models here.
class Detail(models.Model):
    product = models.FloatField(default=0)
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)


