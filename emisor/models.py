from django.db import models
from django.conf import settings

# Create your models here.
class Emisor(models.Model):
    rfc = models.TextField(blank=True)
    nombre = models.TextField(blank=True)
    direccion = models.TextField(blank=True)
    cp = models.IntegerField()
    regimenfiscal = models.TextField(default='')
    certificado = models.TextField(default='')
    filekey = models.TextField(default='')
    passcertificado = models.TextField(default='')
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
