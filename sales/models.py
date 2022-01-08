from django.db import models
from django.conf import settings
from django.utils.timezone import now


# Create your models here.
class Sale(models.Model):
    serie = models.TextField(default='')
    folio = models.TextField(default='')
    fecha = models.DateTimeField(default=now, blank=True)
    formapago = models.TextField(default='')
    condicionesdepago = models.TextField(default='')
    subtotal = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    moneda = models.TextField(default='')
    tipodecomprobante = models.TextField(default='')
    metodopago = models.TextField(default='')
    lugarexpedicion = models.TextField(default='')
    totalimpuestostrasladados = models.FloatField(default=0)
    totalimpuestosretenidos = models.FloatField(default=0)
    total = models.FloatField(default=0)
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    statusv    = models.TextField(default='')
    statuscfdi = models.TextField(default='')
    xml = models.TextField(default='')
    pdf = models.TextField(default='')
    complpago = models.TextField(default='')
    complneg  = models.TextField(default='')
    receptor = models.ForeignKey('receptor.Receptor', null=True, related_name='receptor', on_delete=models.CASCADE)


# Product models here.
class Detail(models.Model):
    product = models.FloatField(default=0)
    cantidad = models.FloatField(default=0)
    precio = models.FloatField(default=0)
    importe = models.FloatField(default=0) 
    url = models.URLField(default='')
    codigosat = models.TextField(default='')
    noidentificacion = models.TextField(default='')
    claveunidad = models.TextField(default='')
    descuento = models.FloatField(default=0)
    trasladoiva = models.FloatField(default=0)
    retiva = models.FloatField(default=0)
    ieps = models.FloatField(default=0)


    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)


