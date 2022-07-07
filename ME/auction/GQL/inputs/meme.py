import graphene

class MemeInput(graphene.InputObjectType):

    name = graphene.String(required = True)
    description = graphene.String()
    owner = graphene.ID(required = True)
