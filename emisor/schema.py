import graphene
from graphene_django import DjangoObjectType
from .models import Emisor
from users.schema import UserType
from django.db.models import Q

class EmisorType(DjangoObjectType):
    class Meta:
        model = Emisor

class Query(graphene.ObjectType):
    emisor = graphene.List(EmisorType)
    emisorme = graphene.Field(EmisorType)
    emisorcer = graphene.Field(EmisorType, rfc=graphene.String())

    def resolve_emisorcer(self, info, rfc=None):
        
        currentEmisor = Emisor.objects.filter(rfc=rfc).first()
        return currentEmisor



    def resolve_emisorme(self, info):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')
        
        currentEmisor = Emisor.objects.filter(posted_by=user).first()
        return currentEmisor



    def resolve_emisor(self, info, **kwargs):
        return Emisor.objects.all()

class CreateEmisor(graphene.Mutation):
    id = graphene.Int()

    rfc = graphene.String()
    nombre = graphene.String()
    direccion = graphene.String()
    codigopostal = graphene.Int()
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
      codigopostal = graphene.Int()
      regimenfiscal = graphene.String()
      certificado = graphene.String()
      filekey = graphene.String()
      passcertificado = graphene.String()


    #3
    def mutate(self, info, rfc, nombre, direccion, codigopostal, regimenfiscal, certificado, filekey, passcertificado):
        user = info.context.user or None
        print(user)
        currentEmisor = Emisor.objects.filter(posted_by=user).first()
        print (currentEmisor)

        emisor = Emisor(
            #id=currentEmisor.id,
            rfc=rfc, 
            nombre=nombre,
            direccion=direccion,
            cp=codigopostal,
            regimenfiscal=regimenfiscal,
            certificado=certificado,
            filekey=filekey,
            passcertificado=passcertificado,
            posted_by = user
            )

        if currentEmisor:
            emisor.id = currentEmisor.id

        emisor.save()

        return CreateEmisor(
            id=emisor.id,
            rfc=emisor.rfc,
            nombre=emisor.nombre,
            direccion=emisor.direccion,
            codigopostal=emisor.cp,
            regimenfiscal=emisor.regimenfiscal,
            posted_by=emisor.posted_by
        )

#4
class Mutation(graphene.ObjectType):
    create_emisor = CreateEmisor.Field()
