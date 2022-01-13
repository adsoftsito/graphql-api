from django.db import models

# Create your models here.
class ClaveUnidad(models.Model):
    claveunidad = models.TextField(default='', blank=True, null=True)
    nombre = models.TextField(default='', blank=True, null=True)
    descripcion = models.TextField(default='', blank=True, null=True)
    simbolo = models.TextField(default='', blank=True, null=True)

class ClaveProdServ(models.Model):
    claveprodserv = models.TextField(default='', blank=True, null=True)
    descripcion = models.TextField(default='', blank=True, null=True)
    sinonimos = models.TextField(default='', blank=True, null=True)

