import graphene
from ME.auction.GQL.inputs.bid import CreateBidInput
from ME.auction.models import Auction, Bid
from ME.auction.GQL.types import BidType, MemeType
from ME.core.models import Profile

class CreateBid(graphene.Mutation):

    class Arguments:
        information = CreateBidInput(required = True)
    
    bid = graphene.Field(MemeType)

    @staticmethod
    def save(root, info, information = None):

        profile = Profile.objects.get(id = information.profile)
        auction = Auction.objects.get(id = information.auction)
        bid = Bid(
            profile = profile,
            auction = auction,
            value = information.value
        )
        bid.save()

        return CreateBid(bid = bid)