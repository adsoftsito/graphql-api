import graphene
from graphene_django import DjangoObjectType
from .models import Link
from users.schema import UserType
from django.db.models import Q
from cat40.models import ClaveUnidad, ClaveProdServ

class LinkType(DjangoObjectType):
    class Meta:
        model = Link

class Query(graphene.ObjectType):
    links = graphene.List(LinkType, search=graphene.String())

    def resolve_links(self, info, search=None, **kwargs):
        user = info.context.user 
        if user.is_anonymous:
            raise Exception('Not logged in!')

        print (user)

        if (search=="*"):
            filter = (
                Q(posted_by=user)
            )

            return Link.objects.filter(filter)[:10]
        else:
            filter = (
                Q(posted_by=user) & Q(description__icontains=search)
            )
            return Link.objects.filter(filter)

           

class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    precio = graphene.Float()

    codigosat = graphene.String()
    noidentificacion = graphene.String()
    claveunidad = graphene.String()
    descuento = graphene.Float()
    trasladoiva = graphene.Float()
    retiva = graphene.Float()
    ieps = graphene.Float()

    posted_by = graphene.Field(UserType)


    #2
    class Arguments:
        idprod = graphene.Int()
        url = graphene.String()
        description = graphene.String()
        precio = graphene.Float()
        codigosat = graphene.Int()
        noidentificacion = graphene.String()
        claveunidad = graphene.Int()
        descuento = graphene.Float()
        codigobarras = graphene.String()
        trasladoiva = graphene.Float()
        trasladoieps = graphene.Float()
        retencioniva = graphene.Float()
        retencionisr = graphene.Float()
        retencionieps = graphene.Float()
        existencias = graphene.Float()
        stockmin = graphene.Float()
        stockmax = graphene.Float()

    #3
    def mutate(self, info, idprod, url, description, precio, codigosat, noidentificacion, claveunidad, descuento, codigobarras, trasladoiva, trasladoieps, retencioniva, retencionisr, retencionieps, existencias, stockmin, stockmax):
        user = info.context.user 
        if user.is_anonymous:
            raise Exception('Not logged in!')


        currentProduct = Link.objects.filter(id=idprod).first()
        
        unidad = ClaveUnidad.objects.filter(id=claveunidad).first()
        if not unidad:
            raise Exception('Clave unidad de medida no existe!')
        
        codigo = ClaveProdServ.objects.filter(id=codigosat).first()
        if not codigo:
            raise Exception('Codigo Sat no existe!')


        link = Link(
            url=url, 
            description=description,
            precio=precio,
            codigosat=codigo,
            noidentificacion=noidentificacion,
            claveunidad=unidad,
            descuento=descuento,
            codigobarras=codigobarras,
            trasladoiva=trasladoiva,
            trasladoieps=trasladoieps,
            retencionisr=retencionisr,
            retencioniva=retencioniva,
            retencionieps=retencionieps,
            existencias=existencias,
            stockmin=stockmin,
            stockmax=stockmax,
            posted_by = user
            )

        if currentProduct:
            link.id = idprod
   
        link.save()
       
        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            precio=link.precio,
            codigosat=link.codigosat,
            noidentificacion=link.noidentificacion,
            claveunidad=link.claveunidad,
            descuento=link.descuento,
            trasladoiva=link.trasladoiva,
            retiva=link.retencioniva,
            ieps=link.retencionieps,
            posted_by=link.posted_by
        )

#4
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
