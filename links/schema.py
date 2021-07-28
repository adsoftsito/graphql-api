import graphene
from graphene_django import DjangoObjectType
from .models import Link
from users.schema import UserType

class LinkType(DjangoObjectType):
    class Meta:
        model = Link

class Query(graphene.ObjectType):
    links = graphene.List(LinkType)

    def resolve_links(self, info, **kwargs):
        return Link.objects.all()

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

    #3
    def mutate(self, info, url, description, precio, codigosat, noidentificacion, claveunidad,
        descuento, trasladoiva, retiva, ieps):
        user = info.context.user or None

        link = Link(
            url=url, 
            description=description,
            precio=precio,
            codigosat=codigosat,
            noidentificacion=noidentificacion,
            claveunidad=claveunidad,
            descuento=descuento,
            trasladoiva=trasladoiva,
            retiva=retiva,
            ieps=ieps,
            posted_by = user
            )
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
            retiva=link.retiva,
            ieps=link.ieps,
            posted_by=link.posted_by
        )

#4
class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
