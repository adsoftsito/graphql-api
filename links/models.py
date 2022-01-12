from django.db import models
from django.conf import settings

# Create your models here.
class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    precio = models.FloatField(default=0)

    codigosat = models.TextField(default='01010101')
    noidentificacion = models.TextField(default='')
    codigobarras = models.TextField(default='')

    claveunidad = models.TextField(default='H87')
    descripunidad = models.TextField(default='Pieza')
    descuento = models.FloatField(default=0)
    trasladoiva = models.FloatField(default=0)
    retiva = models.FloatField(default=0)
    ieps = models.FloatField(default=0)

    existencias = models.FloatField(default=0)
    stockmin = models.FloatField(default=1)
    stockmax = models.FloatField(default=1)
    
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


