import graphene
from graphene_django import DjangoObjectType
from django.db.models import Q

from .models import Estacion
from .models import Colonia
from .models import Localidad
from .models import Municipio


class EstacionType(DjangoObjectType):
    class Meta:
        model = Estacion

class ColoniaType(DjangoObjectType):
    class Meta:
        model = Colonia

class LocalidadType(DjangoObjectType):
    class Meta:
        model = Localidad

class MunicipioType(DjangoObjectType):
    class Meta:
        model = Municipio


class Query(graphene.ObjectType):
    estaciones = graphene.List(EstacionType)

    def resolve_estaciones(self, info, **kwargs):
        return Estacion.objects.all()

    colonias = graphene.List(ColoniaType, codigopostal = graphene.String())

    def resolve_colonias(self, info, codigopostal=None,  **kwargs):
        filter = (
            Q(codigopostal__exact=codigopostal) 
        )
        return Colonia.objects.filter(filter)


    localidades = graphene.List(LocalidadType, estado = graphene.String())

    def resolve_localidades(self, info, estado=None,  **kwargs):
        filter = (
            Q(estado__exact=estado)
        )
        return Localidad.objects.filter(filter)

    municipios = graphene.List(MunicipioType, estado = graphene.String())

    def resolve_municipios(self, info, estado=None,  **kwargs):
        filter = (
            Q(estado__exact=estado)
        )
        return Municipio.objects.filter(filter)


