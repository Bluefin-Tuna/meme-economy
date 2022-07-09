import graphene
from auction.GQL.inputs.auction import CreateAuctionInput, UpdateAuctionInput, DeleteAuctionInput
from auction.models import Auction
from auction.GQL.types import AuctionType


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
        if(hasattr(information, "limit")):
            auction.limit = int(information.limit)
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
            
            for key in information:
                exec(f'auction.{key} = information.{key}')
            auction.save()

            return UpdateAuction(auction = auction)
        
        return UpdateAuction(auction = None)


class DeleteAuction(graphene.Mutation):

    class Arguments:
        information = DeleteAuctionInput(required = True)

    auction = graphene.Field(AuctionType)

    @staticmethod
    def mutate(root, info, information = None):

        auction = Auction.objects.get(id = information.id)
        auction.delete()

        return None



class AuctionMutation(graphene.ObjectType):

    create_auction = CreateAuction.Field()
    update_auction = UpdateAuction.Field()
    delete_auction = DeleteAuction.Field()