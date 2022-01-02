import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

from .models import Estacion
from .models import Colonia


class EstacionType(DjangoObjectType):
    class Meta:
        model = Estacion

class ColoniaType(DjangoObjectType):
    class Meta:
        model = Colonia

class Query(graphene.ObjectType):
    estaciones = graphene.List(EstacionType)

    def resolve_estaciones(self, info, **kwargs):
        return Estacion.objects.all()

    colonias = graphene.List(ColoniaType, codigopostal = graphene.String())

    def resolve_colonias(self, info, codigopostal=None,  **kwargs):
        #if codigopostal:
        filter = (
            Q(codigopostal__exact=codigopostal) 
        )
        return Colonia.objects.filter(filter)

        #return Colonia.objects.all()

