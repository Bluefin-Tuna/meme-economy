import graphene
from auction.models import Bid
from auction.GQL.types import BidType

class BidQueries(graphene.ObjectType):

    all_bids = graphene.List(BidType)
    bid = graphene.Field(BidType, id = graphene.Int())

    def resolve_all_bids(self, info, **kwargs):
        return Bid.objects.get()
    
    def resolve_bid(self, info, id):
        return Bid.objects.get(id = id)