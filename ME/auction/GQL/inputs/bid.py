import graphene

class BidInput(graphene.InputObjectType):

    user = graphene.ID(required = True)
    auction = graphene.ID(required = True)
    value = graphene.Int(required = True)