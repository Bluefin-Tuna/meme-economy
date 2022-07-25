import graphene
from auction.models import Bid
from auction.GQL.types import BidType

class BidQuery(graphene.ObjectType):

    all_bids = graphene.List(BidType)
    bid = graphene.Field(BidType, profile = graphene.Int(required = True), auction = graphene.Int(required = True))

    def resolve_all_bids(self, info, **kwargs):
        return Bid.objects.all()
    
    def resolve_bid(self, info, profile, auction):
        return Bid.objects.get(profile = profile, auction = auction)