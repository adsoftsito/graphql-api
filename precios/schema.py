import graphene
from graphene_django import DjangoObjectType
from .models import Lista, Precio
from users.schema import UserType
from django.db.models import Q

class ListaType(DjangoObjectType):
    class Meta:
        model = Lista

class PrecioType(DjangoObjectType):
    class Meta:
        model = Precio


#class ListaOutput(graphene.ObjectType):
#    lista =    graphene.Field(ListaType)
#    precios  = graphene.List(PrecioType)


class Query(graphene.ObjectType):
    listas = graphene.List(ListaType,   search=graphene.String())
    lista  = graphene.Field(ListaType,  listaid=graphene.Int())

    def resolve_listas(self, info, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        print (user)

        filter = (
            Q(posted_by=user)
        )

        return Lista.objects.filter(filter)[:20]

    def resolve_lista(self, info, listaid = None, **kwargs):

        myLista = Lista.objects.filter(id=listaid).first()
        print(myLista)

        return myLista

