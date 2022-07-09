import graphene
from auction.GQL.inputs.bid import CreateBidInput
from auction.models import Auction, Bid
from auction.GQL.types import BidType
from core.models import Profile


class CreateBid(graphene.Mutation):

    class Arguments:
        information = CreateBidInput(required = True)
    
    bid = graphene.Field(BidType)

    @staticmethod
    def mutate(root, info, information = None):

        profile = Profile.objects.get(id = information.profile)
        auction = Auction.objects.get(id = information.auction)
        bid = Bid(
            profile = profile,
            auction = auction,
            value = information.value
        )
        bid.save()

        return CreateBid(bid = bid)



class BidMutation(graphene.ObjectType):

    create_bid = CreateBid.Field()