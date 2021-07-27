import graphene
from graphene_django import DjangoObjectType
from .models import Receptor
from users.schema import UserType
from django.db.models import Q

class ReceptorType(DjangoObjectType):
    class Meta:
        model = Receptor

class Query(graphene.ObjectType):
    receptor = graphene.List(ReceptorType)

    def resolve_receptor(self, info, **kwargs):
        return Receptor.objects.all()

class CreateReceptor(graphene.Mutation):
    id = graphene.Int()

    rfc = graphene.String()
    nombre = graphene.String()
    direccion = graphene.String()
    codigopostal = graphene.Int()
    usocfdi = graphene.String()
    metododepago = graphene.String()
    formadepago = graphene.String()
    tipocomprobante = graphene.String()

    posted_by = graphene.Field(UserType)

    #2
    class Arguments:
      rfc = graphene.String()
      nombre = graphene.String()
      direccion = graphene.String()
      codigopostal = graphene.Int()
      usocfdi = graphene.String()
      metododepago = graphene.String()
      formadepago = graphene.String()
      tipocomprobante = graphene.String()


    #3
    def mutate(self, info, rfc, nombre, direccion, codigopostal, usocfdi, metododepago, formadepago, tipocomprobante):
        user = info.context.user or None
        print(user)
        currentReceptor = Receptor.objects.filter(posted_by=user).first()
        print (currentReceptor)

        receptor = Receptor(
            #id=currentEmisor.id,
            rfc=rfc, 
            nombre=nombre,
            direccion=direccion,
            cp=codigopostal,
            usocfdi=usocfdi,
            metododepago=metododepago,
            formadepago=formadepago,
            tipocomprobante=tipocomprobante,
            posted_by = user
            )

        if currentReceptor:
            receptor.id = currentReceptor.id

        receptor.save()

        return CreateReceptor(
            id=receptor.id,
            rfc=receptor.rfc,
            nombre=receptor.nombre,
            direccion=receptor.direccion,
            codigopostal=receptor.cp,
            posted_by=receptor.posted_by
        )

#4
class Mutation(graphene.ObjectType):
    create_receptor = CreateReceptor.Field()
