import graphene
from graphene_django import DjangoObjectType
from .models import Emisor
from users.schema import UserType

class EmisorType(DjangoObjectType):
    class Meta:
        model = Emisor

class Query(graphene.ObjectType):
    emisors = graphene.List(EmisorType)

    def resolve_links(self, info, **kwargs):
        return Emisor.objects.all()

class CreateEmisor(graphene.Mutation):
    id = graphene.Int()

    rfc = graphene.String()
    nombre = graphene.String()
    direccion = graphene.String()
    cp = graphene.Int()
    regimenfiscal = graphene.String()
    certificado= graphene.String()
    filekey = graphene.String()
    passcertificado = graphene.String()

    posted_by = graphene.Field(UserType)

    #2
    class Arguments:
      rfc = graphene.String()
      nombre = graphene.String()
      direccion = graphene.String()
      cp = graphene.Int()
      #regimenfiscal = graphene.String()
      certificado = graphene.String()
      filekey = graphene.String()
      passcertificado = graphene.String()


    #3
    def mutate(self, info, rfc, nombre, direccion, codigopostal, certificado, filekey, passcertificado):
        user = info.context.user or None

        emisor = Emisor(
            rfc=rfc, 
            nombre=nombre,
            direccion=direccion,
            cp=codigopostal,
            certificado=certificado,
            filekey=filekey,
            passcertificado=passcertificado,
            posted_by = user
            )
        emisor.save()

        return CreateEmisor(
            id=emisor.id,
            rfc=emisor.rfc,
            direccion=emisor.direccion,
            posted_by=emisor.posted_by
        )

#4
class Mutation(graphene.ObjectType):
    create_emisor = CreateEmisor.Field()
