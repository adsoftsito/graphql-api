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
    listas = graphene.List(ListaType,   search=graphene.String(), tipolista=graphene.Int())
    lista  = graphene.Field(ListaType,  listaid=graphene.Int(), tipolista=graphene.Int())

    def resolve_listas(self, info, search=graphene.String(), tipolista=None, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        print (user)
        if (search=="*"):
            filter = (
                Q(posted_by=user) &  Q(tipolista=tipolista)
            )
        else:
            filter = (
                Q(posted_by=user) & Q(descripcion__icontains=search) &  Q(tipolista=tipolista)
            )


        return Lista.objects.filter(filter)[:20]

    def resolve_lista(self, info, listaid = None, tipolista=None,  **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        filter = (
            Q(posted_by=user) & Q(id=listaid) & Q(tipolista=tipolista)
        )

        myLista = Lista.objects.filter(filter).first()
        print(myLista)

        return myLista

