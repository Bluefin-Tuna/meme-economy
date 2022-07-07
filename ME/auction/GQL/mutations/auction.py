import graphene
from ME.auction.GQL.inputs.auction import CreateAuctionInput, UpdateAuctionInput, DeleteAuctionInput
from ME.auction.models import Auction
from ME.auction.GQL.types import AuctionType

class CreateAuction(graphene.Mutation):

    class Arguments:
        information = CreateAuctionInput(required = True)

    auction = graphene.Field(AuctionType)

    @staticmethod
    def mutate(root, info, information = None):
        
        auction = Auction(
            initial_price = information.initial_price,
            starts_at = information.starts_at,
            ends_at = information.ends_at,
        )
        auction.limit = information.limit

        auction.save()

        return CreateAuction(auction = auction)

class UpdateAuction(graphene.Mutation):

    class Arguments: 
        information = UpdateAuctionInput(required = True)
    
    auction = graphene.Field(AuctionType)

    @staticmethod
    def mutate(root, info, information = None):
        
        auction = Auction.objects.get(id = information.id)

        if(auction):
            auction.
        