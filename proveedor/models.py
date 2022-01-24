from django.db import models
from django.conf import settings

# Create your models here.
class Proveedor(models.Model):
    rfc = models.TextField(blank=True)
    nombre = models.TextField(blank=True)
    direccion = models.TextField(blank=True)
    cp = models.IntegerField()
    usocfdi = models.TextField(default='G03')
    metododepago = models.TextField(default='PUE')
    formadepago = models.TextField(default='01')
    tipocomprobante = models.TextField(default='E')
    listacompra = models.ForeignKey('precios.Lista', related_name='proveedor', null=True, on_delete=models.CASCADE)

    contacto = models.TextField(default='')
    diascredito = models.IntegerField(default=0)
    descuento = models.FloatField(default=0)

    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
