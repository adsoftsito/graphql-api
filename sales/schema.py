import graphene
from graphene_django import DjangoObjectType
from .models import Sale
from .models import Detail
from users.schema import UserType
from receptor.models import Receptor
from links.models import Link

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
#    url = graphene.String(required=True)
#    codigosat = graphene.String(required=True)
#    noidentificacion = graphene.String(required=True)
#    claveunidad = graphene.String(required=True)
    descuento = graphene.Float(required=True) 
#    trasladoiva = graphene.Float(required=True)
#    retiva = graphene.Float(required=True)
#    ieps = graphene.Float(required=True)



class DetailType(DjangoObjectType):
    class Meta:
        model = Detail

class SaleType(DjangoObjectType):
    class Meta:
        model = Sale

class ReceptorType(DjangoObjectType):
    class Meta:
        model = Receptor

#class SaleOutput(graphene.ObjectType):
#    sale =    graphene.Field(SaleType)
#    detail  = graphene.List(DetailType)

class Query(graphene.ObjectType):
    sales = graphene.List(SaleType, search = graphene.String())
    sale  = graphene.Field(SaleType, saleid = graphene.Int())

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
    
    def resolve_sale(self, info, saleid = None, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        mySale = Sale.objects.filter(id=saleid).first()
        if not mySale:
            raise Exception('Sale Id no existe!')

        #print(mySale)
        #print (mySale.details.all())
        #print (mySale.details.first().id)

        return mySale


class UpdateSale(graphene.Mutation):
    id = graphene.Int()
    statuscfdi = graphene.String()
    xml = graphene.String()
    pdf = graphene.String()

    class Arguments:
        saleid = graphene.Int()
        statuscfdi = graphene.String()
        xml = graphene.String()
        pdf = graphene.String()

    def mutate(self, info, saleid, statuscfdi, xml, pdf):

        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        mySale = Sale.objects.filter(id=saleid).first()
        if not mySale:
            raise Exception('Invalid Sale id!')
        print (mySale)

        #link = Link(
        #    url=url,
        #    posted_by = user
        #    )

        mySale.statuscfdi = statuscfdi
        mySale.xml = xml
        mySale.pdf = pdf

        mySale.save()

        return UpdateSale(
            id=mySale.id,
            statuscfdi=mySale.statuscfdi,
            xml=mySale.xml,
            pdf=mySale.pdf,
            )


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
        
        for product in products:        
            productid = product["product"]
            myproduct = Link.objects.filter(id=productid).first()
            if not myproduct:
                raise Exception('Invalid Product !' + str(productid))


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
            productid = product["product"]
            myproduct = Link.objects.filter(id=productid).first()

            myproduct = Detail(
                product = myproduct,
                cantidad = product["cantidad"],
                precio = product["precio"],
                importe = product["importe"],
                descuento = product["descuento"],
                trasladoiva = 0.0,
                trasladoieps = 0.0,
                retencioniva = 0.0,
                retencionisr = 0.0,
                retencionieps = 0.0,
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
    update_sale = UpdateSale.Field()

