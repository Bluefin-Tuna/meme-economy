import graphene

class CreateBidInput(graphene.InputObjectType):

    user = graphene.ID(required = True)
    auction = graphene.ID(required = True)
    value = graphene.Int(required = True)