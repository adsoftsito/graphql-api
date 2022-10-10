import graphene
from graphene_django import DjangoObjectType
from .models import Link, Marca, Linea
from users.schema import UserType
from django.db.models import Q
from cat40.models import ClaveUnidad, ClaveProdServ

class LinkType(DjangoObjectType):
    class Meta:
        model = Link

class MarcaType(DjangoObjectType):
    class Meta:
        model = Marca

class LineaType(DjangoObjectType):
    class Meta:
        model = Linea


class Query(graphene.ObjectType):
    links = graphene.List(LinkType, search=graphene.String())
    marcas = graphene.List(MarcaType, search=graphene.String())
    lineas = graphene.List(LineaType, search=graphene.String())

    def resolve_links(self, info, search=None, **kwargs):
        user = info.context.user 
        if user.is_anonymous:
            raise Exception('Not logged in!')

        print (user)

        if (search=="*"):
            filter = (
                Q(posted_by=user)
            )

            return Link.objects.filter(filter)[:10]
        else:
            filter = (
                Q(posted_by=user) & Q(description__icontains=search)
            )
            return Link.objects.filter(filter)

           
    def resolve_marcas(self, info, search=None, **kwargs):
        user = info.context.user 
        if user.is_anonymous:
            raise Exception('Not logged in!')

        print (user)

        if (search=="*"):
            filter = (
                Q(posted_by=user)
            )

            return Marca.objects.filter(filter)[:10]
        else:
            filter = (
                Q(posted_by=user) & Q(description__icontains=search)
            )
            return Marca.objects.filter(filter)

           
    def resolve_lineas(self, info, search=None, **kwargs):
        user = info.context.user 
        if user.is_anonymous:
            raise Exception('Not logged in!')

        print (user)

        if (search=="*"):
            filter = (
                Q(posted_by=user)
            )

            return Linea.objects.filter(filter)[:10]
        else:
            filter = (
                Q(posted_by=user) & Q(description__icontains=search)
            )
            return Linea.objects.filter(filter)

           

class CreateLink(graphene.Mutation):
    id = graphene.Int()
    url = graphene.String()
    description = graphene.String()
    precio = graphene.Float()
    modelo = graphene.String()
    marca = graphene.Field(MarcaType)
    linea = graphene.Field(LineaType)

    codigosat = graphene.String()
    noidentificacion = graphene.String()
    claveunidad = graphene.String()
    descuento = graphene.Float()
    trasladoiva = graphene.Float()
    retiva = graphene.Float()
    ieps = graphene.Float()

    posted_by = graphene.Field(UserType)


    #2
    class Arguments:
        idprod = graphene.Int()
        url = graphene.String()
        description = graphene.String()
        modelo = graphene.String()
        marca = graphene.Int()
        linea = graphene.Int()

        precio = graphene.Float()
        codigosat = graphene.Int()
        noidentificacion = graphene.String()
        claveunidad = graphene.Int()
        descuento = graphene.Float()
        codigobarras = graphene.String()
        trasladoiva = graphene.Float()
        trasladoieps = graphene.Float()
        retencioniva = graphene.Float()
        retencionisr = graphene.Float()
        retencionieps = graphene.Float()
        existencias = graphene.Float()
        stockmin = graphene.Float()
        stockmax = graphene.Float()

    #3
    def mutate(self, info, idprod, url, description, precio, codigosat, noidentificacion, claveunidad, descuento, codigobarras, trasladoiva, trasladoieps, retencioniva, retencionisr, retencionieps, existencias, stockmin, stockmax, modelo, marca, linea):
        user = info.context.user 
        if user.is_anonymous:
            raise Exception('Not logged in!')


        currentProduct = Link.objects.filter(id=idprod).first()
        
        unidad = ClaveUnidad.objects.filter(id=claveunidad).first()
        if not unidad:
            raise Exception('Clave unidad de medida no existe!')
        
        codigo = ClaveProdServ.objects.filter(id=codigosat).first()
        if not codigo:
            raise Exception('Codigo Sat no existe!')

        mymarca = Marca.objects.filter(id=marca).first()
        if not mymarca:
            raise Exception('Marca no existe!')

        mylinea = Linea.objects.filter(id=linea).first()
        if not mylinea:
            raise Exception('Linea no existe!')


        link = Link(
            url=url, 
            description=description,
            precio=precio,
            codigosat=codigo,
            noidentificacion=noidentificacion,
            claveunidad=unidad,
            descuento=descuento,
            codigobarras=codigobarras,
            trasladoiva=trasladoiva,
            trasladoieps=trasladoieps,
            retencionisr=retencionisr,
            retencioniva=retencioniva,
            retencionieps=retencionieps,
            existencias=existencias,
            stockmin=stockmin,
            stockmax=stockmax,
            modelo=modelo,
            marca=mymarca,
            linea=mylinea,
            posted_by = user
            )

        if currentProduct:
            link.id = idprod
   
        link.save()
       
        return CreateLink(
            id=link.id,
            url=link.url,
            description=link.description,
            modelo=link.modelo,
            marca=link.marca,
            linea=link.linea,
            precio=link.precio,
            codigosat=link.codigosat,
            noidentificacion=link.noidentificacion,
            claveunidad=link.claveunidad,
            descuento=link.descuento,
            trasladoiva=link.trasladoiva,
            retiva=link.retencioniva,
            ieps=link.retencionieps,
            posted_by=link.posted_by
        )

#4

class CreateMarca(graphene.Mutation):
    id = graphene.Int()
    description = graphene.String()
    posted_by = graphene.Field(UserType)


    #2
    class Arguments:
        idmarca = graphene.Int()
        description = graphene.String()

    #3
    def mutate(self, info, idmarca, description):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')


        currentMarca = Marca.objects.filter(id=idmarca).first()
        marca = Marca(
            description=description,
            posted_by = user
            )

        if currentMarca:
            marca.id = idmarca
   
        marca.save()
       
        return CreateMarca(
            id=marca.id,
            description=marca.description,
            posted_by=marca.posted_by
        )

class CreateLinea(graphene.Mutation):
    id = graphene.Int()
    description = graphene.String()
    posted_by = graphene.Field(UserType)


    #2
    class Arguments:
        idlinea = graphene.Int()
        description = graphene.String()

    #3
    def mutate(self, info, idlinea, description):
        user = info.context.user
        if user.is_anonymous:
            raise Exception('Not logged in!')


        currentLinea = Linea.objects.filter(id=idlinea).first()
        linea = Linea(
            description=description,
            posted_by = user
            )

        if currentLinea:
            linea.id = idlinea
   
        linea.save()
       
        return CreateLinea(
            id=linea.id,
            description=linea.description,
            posted_by=linea.posted_by
        )


class Mutation(graphene.ObjectType):
    create_link = CreateLink.Field()
    create_marca = CreateMarca.Field()
    create_linea = CreateLinea.Field()

