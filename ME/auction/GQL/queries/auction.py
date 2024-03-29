import graphene
from auction.models import Auction
from auction.GQL.types import AuctionType

class AuctionQuery(graphene.ObjectType):

    all_auctions = graphene.List(AuctionType)
    auction = graphene.Field(AuctionType, id = graphene.Int())

    def resolve_all_auctions(self, info, **kwargs):
        return Auction.objects.all()
    
    def resolve_auction(self, info, id):
        return Auction.objects.get(id = id)