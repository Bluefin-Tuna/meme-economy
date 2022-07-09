import graphene
from auction.GQL import AuctionQueries, AuctionMutations
from core.GQL import CoreQueries, CoreMutations

class Queries(AuctionQueries, CoreQueries, graphene.ObjectType):
    pass

class Mutations(AuctionMutations, CoreMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query = Queries, mutation = Mutations)