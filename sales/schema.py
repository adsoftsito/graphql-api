import graphene
from graphene_django import DjangoObjectType
from .models import Sale
from .models import Detail
from users.schema import UserType
from receptor.models import Receptor

#from graphene import ObjectType
from graphene.types.generic import GenericScalar
import json
from django.core import serializers
from django.db.models import Q



class DetailInput(graphene.InputObjectType):
#    class Meta:
#        model = Detail
#        fields = ('product','cantidad','precio')
    product = graphene.Int(required=True)
    cantidad = graphene.Float(required=True)
    precio = graphene.Float(required=True)
    importe = graphene.Float(required=True)
    url = graphene.String(required=True)
    codigosat = graphene.String(required=True)
    noidentificacion = graphene.String(required=True)
    claveunidad = graphene.String(required=True)
    descuento = graphene.Float(required=True) 
    trasladoiva = graphene.Float(required=True)
    retiva = graphene.Float(required=True)
    ieps = graphene.Float(required=True)


#input DetailInput {
#    product: Int,
#    cantidad: Float,
#    precio: Float
#}

#class DetailInput(DjangoObjectType):
#    class Meta:
#        model = Detail

class SaleType(DjangoObjectType):
    class Meta:
        model = Sale

class ReceptorType(DjangoObjectType):
    class Meta:
        model = Receptor

class Query(graphene.ObjectType):
    sales = graphene.List(SaleType, search = graphene.String())

    def resolve_sales(self, info, search = None, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        if (search=="*"):
            filter = (
                Q(posted_by=user)
            )

            return Sale.objects.filter(filter)[:20]
        else:
            filter = (
                Q(posted_by=user) & Q(serie__icontains=search)
            )
            return Sale.objects.filter(filter)


class CreateSale(graphene.Mutation):
    id = graphene.Int()

    serie = graphene.String()
    folio = graphene.String()
    # fecha = models.DateTimeField(default=now, blank=True)
    formapago = graphene.String()
    condicionesdepago = graphene.String()
    subtotal = graphene.Float()
    descuento = graphene.Float()
    moneda = graphene.String()
    tipodecomprobante = graphene.String()
    metodopago = graphene.String()
    lugarexpedicion = graphene.String()
    totalimpuestostrasladados = graphene.Float()
    totalimpuestosretenidos = graphene.Float()
    total = graphene.Float()

    posted_by = graphene.Field(UserType)
    #receptor =  graphene.Field(ReceptorType)

    #products = graphene.List(Detail)

    #2
    class Arguments:
        serie = graphene.String()
        folio = graphene.String()
        formapago = graphene.String()
        condicionesdepago = graphene.String()
        subtotal = graphene.Float()
        descuento = graphene.Float()
        moneda = graphene.String()
        tipodecomprobante = graphene.String()
        metodopago = graphene.String()
        lugarexpedicion = graphene.String()
        totalimpuestostrasladados = graphene.Float()
        totalimpuestosretenidos = graphene.Float()
        total = graphene.Float()
        receptor_id = graphene.Int()


        products = graphene.List(DetailInput)
        #products = GenericScalar() 
    #3
    def mutate(self, info, serie, folio, formapago, condicionesdepago, subtotal, descuento, moneda, tipodecomprobante, 
              metodopago, lugarexpedicion, totalimpuestostrasladados, totalimpuestosretenidos, total, receptor_id, products):

        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        myreceptor = Receptor.objects.filter(id=receptor_id).first()
        if not myreceptor:
            raise Exception('Invalid Receptor!')
        print (myreceptor)

        sale = Sale.objects.create(
            serie=serie,
            folio=folio,
            formapago=formapago,
            condicionesdepago=condicionesdepago,
            subtotal=subtotal, 
            descuento=descuento,
            moneda=moneda,
            tipodecomprobante=tipodecomprobante,
            metodopago=metodopago,
            lugarexpedicion=lugarexpedicion,
            totalimpuestostrasladados=totalimpuestostrasladados,
            totalimpuestosretenidos=totalimpuestosretenidos,
            total=total,
            receptor=myreceptor,
            posted_by = user
            )
        #sale.save()

        myproducts = []
        for product in products:        
          myproduct = Detail(
              product = product["product"],
              cantidad = product["cantidad"],
              precio = product["precio"],
              importe = product["importe"],
              url = product["url"],
              codigosat = product["codigosat"],
              noidentificacion = product["noidentificacion"],
              claveunidad = product["claveunidad"],
              descuento = product["descuento"],
              trasladoiva = product["trasladoiva"],
              retiva = product["retiva"],
              ieps = product["ieps"],

              sale = sale
              )
          myproduct.save()
          myproducts.append(myproduct)
          #print (product["product"])



        return CreateSale(
            id=sale.id,
            subtotal=sale.subtotal,
            total=sale.total,
            posted_by=sale.posted_by,
           # receptor=sale.receptor
           # products=myproducts
            )

#4
class Mutation(graphene.ObjectType):
    create_sale = CreateSale.Field()

