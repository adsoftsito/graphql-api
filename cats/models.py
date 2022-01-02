from django.db import models

# Create your models here.
class Estacion(models.Model):
    clave = models.TextField(blank=True)
    description = models.TextField(blank=True)
    clave_transporte = models.TextField(blank=True)
    nacionalidad = models.TextField(blank=True)
    designador_iata = models.TextField(blank=True)
    linea_ferrea = models.TextField(blank=True)

