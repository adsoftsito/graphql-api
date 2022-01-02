import graphene
from graphene_django import DjangoObjectType

from .models import Estacion


class LinkEstacion(DjangoObjectType):
    class Meta:
        model = Estacion


class Query(graphene.ObjectType):
    estaciones = graphene.List(LinkEstacion)

    def resolve_estaciones(self, info, **kwargs):
        return Estacion.objects.all()
