import graphene
from graphene_django import DjangoObjectType
from .models import Proveedor
from users.schema import UserType
from django.db.models import Q

class ProveedorType(DjangoObjectType):
    class Meta:
        model = Proveedor

class Query(graphene.ObjectType):
    proveedores = graphene.List(ProveedorType, search=graphene.String())

    def resolve_proveedores(self, info, search=None, **kwargs):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')

        print (user)

        if (search=="*"):
            filter = (
                Q(posted_by=user)
            )

            return Proveedor.objects.filter(filter)[:10]
        else:
            filter = (
                Q(posted_by=user) & Q(nombre__icontains=search)
            )
            return Proveedor.objects.filter(filter)



class CreateProveedor(graphene.Mutation):
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
      idprov = graphene.Int()
      rfc = graphene.String()
      nombre = graphene.String()
      direccion = graphene.String()
      codigopostal = graphene.Int()
      usocfdi = graphene.String()
      metododepago = graphene.String()
      formadepago = graphene.String()
      tipocomprobante = graphene.String()
      contacto = graphene.String()
      diascredito = graphene.Int()
      descuento = graphene.Float()


    #3
    def mutate(self, info, idprov, rfc, nombre, direccion, codigopostal, usocfdi, metododepago, formadepago, tipocomprobante, contacto, diascredito, descuento):
        user = info.context.user or None
        print(user)


        currentProveedor = Proveedor.objects.filter(id=idprov).first()
        print (currentProveedor)

        proveedor = Proveedor(
            #id=currentEmisor.id,
            rfc=rfc, 
            nombre=nombre,
            direccion=direccion,
            cp=codigopostal,
            usocfdi=usocfdi,
            metododepago=metododepago,
            formadepago=formadepago,
            tipocomprobante=tipocomprobante,
            contacto=contacto,
            diascredito=diascredito,
            descuento=descuento,
            posted_by = user
            )

        if currentProveedor:
            proveedor.id = currentProveedor.id

        proveedor.save()

        return CreateProveedor(
            id=proveedor.id,
            rfc=proveedor.rfc,
            nombre=proveedor.nombre,
            direccion=proveedor.direccion,
            codigopostal=proveedor.cp,
            posted_by=proveedor.posted_by
        )

#4
class Mutation(graphene.ObjectType):
    create_proveedor = CreateProveedor.Field()
