import graphene
from graphene_django import DjangoObjectType
from .models import Sale
from users.schema import UserType

class SaleType(DjangoObjectType):
    class Meta:
        model = Sale

class Query(graphene.ObjectType):
    sales = graphene.List(SaleType)

    def resolve_sales(self, info, **kwargs):
        return Sale.objects.all()

class CreateSale(graphene.Mutation):
    id = graphene.Int()
    subtotal = graphene.Float()
    iva = graphene.Float()
    total = graphene.Float()
    posted_by = graphene.Field(UserType)

    #2
    class Arguments:
        subtotal = graphene.Float()
        iva = graphene.Float()
        total = graphene.Float()

    #3
    def mutate(self, info, subtotal, iva, total):
        user = info.context.user or None

        sale = Sale(
            subtotal=subtotal, 
            iva=iva,
            total=total,
            posted_by = user
            )
        sale.save()

        return CreateSale(
            id=sale.id,
            subtotal=sale.subtotal,
            iva=sale.iva,
            total=sale.total,
            posted_by=sale.posted_by
        )

#4
class Mutation(graphene.ObjectType):
    create_sale = CreateSale.Field()

