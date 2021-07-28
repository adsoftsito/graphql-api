from django.db import models
from django.conf import settings

# Create your models here.
class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)
    precio = models.FloatField(default=0)

    codigosat = models.TextField(default='')
    noidentificacion = models.TextField(default='')
    claveunidad = models.TextField(default='')
    descuento = models.FloatField(default=0)
    trasladoiva = models.FloatField(default=0)
    retiva = models.FloatField(default=0)
    ieps = models.FloatField(default=0)

    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)


