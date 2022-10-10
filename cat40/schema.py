import graphene
from graphene_django import DjangoObjectType
from .models import ClaveUnidad, ClaveProdServ 
from django.db.models import Q


class ClaveUnidadType(DjangoObjectType):
    class Meta:
        model = ClaveUnidad

class ClaveProdServType(DjangoObjectType):
    class Meta:
        model = ClaveProdServ


class Query(graphene.ObjectType):
    claveunidades = graphene.List(ClaveUnidadType, search=graphene.String())
    claveprodserv = graphene.List(ClaveProdServType, search=graphene.String())

    def resolve_claveunidades(self, info, search=None, **kwargs):
        user = info.context.user 
        if user.is_anonymous:
            raise Exception('Not logged in!')

        print (user)

        if (search):
            filter = (
                Q(nombre__icontains=search)
            )

            return ClaveUnidad.objects.filter(filter)[:50]
        else:
            return ClaveUnidad.objects.all()[:20]

    def resolve_claveprodserv(self, info, search=None, **kwargs):
        user = info.context.user 
        if user.is_anonymous:
            raise Exception('Not logged in!')

        print (user)

        if (search):
            filter = (
                Q(descripcion__icontains=search) | Q(sinonimos__icontains=search)
            )

            return ClaveProdServ.objects.filter(filter)[:50]
        else:
            return ClaveProdServ.objects.all()[:20]


