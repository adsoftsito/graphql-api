from django.db import models

# Create your models here.
class Estacion(models.Model):
    clave = models.TextField(blank=True)
    descripcion = models.TextField(blank=True)
    clave_transporte = models.TextField(blank=True, null=True)
    nacionalidad = models.TextField(blank=True, null=True)
    designador_iata = models.TextField(blank=True, null=True)
    linea_ferrea = models.TextField(blank=True, null=True)

class Colonia(models.Model):
    colonia = models.TextField(blank=True, null=True)
    codigopostal = models.TextField(blank=True, null=True)
    nombre_asentamiento = models.TextField(blank=True, null=True)

