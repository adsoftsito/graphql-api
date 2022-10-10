from django.db import models
from django.conf import settings


# Create your models here.
class Lista(models.Model):
    descripcion = models.TextField(default='')
    descuento   = models.FloatField(default=0)
    tipo   = models.TextField(default='')
    tipolista = models.IntegerField(default=0)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    
# Create your models here.
class Precio(models.Model):
    precio = models.FloatField(default=0)
    lista  = models.ForeignKey(Lista, related_name='precios', related_query_name='precio', null=True, on_delete=models.CASCADE)
    producto = models.ForeignKey('links.Link', related_name='producto', null=True, on_delete=models.CASCADE)
#    sale = models.ForeignKey('sales.Sale', related_name='details', related_query_name='detail', on_delete=models.CASCADE)

