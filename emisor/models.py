from django.db import models
from django.conf import settings

# Create your models here.
class Emisor(models.Model):
    rfc = models.TextField(blank=True)
    nombre = models.TextField(blank=True)
    direccion = models.TextField(blank=True)
    cp = models.IntegerField()
    regimenfiscal: models.TextField(blank=False)
    certificado: models.TextField(blank=False)
    filekey = models.TextField(blank=False)
    passcertificado = models.TextField(blank=False)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
