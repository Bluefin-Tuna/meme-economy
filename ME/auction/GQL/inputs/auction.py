import graphene

class CreateAuctionInput(graphene.InputObjectType):
    
    meme = graphene.List(graphene.NonNull(graphene.ID))
    initial_price = graphene.Int(required = True)
    limit = graphene.Int()
    starts_at = graphene.DateTime(required = True)
    ends_at = graphene.DateTime(required = True)


class UpdateAuctionInput(graphene.InputObjectType):

    id = graphene.ID(required = True)
    initial_price = graphene.Int()
    limit = graphene.Int()
    starts_at = graphene.DateTime()
    ends_at = graphene.DateTime()

class DeleteAuctionInput(graphene.InputObjectType):

    id = graphene.ID(required = True)