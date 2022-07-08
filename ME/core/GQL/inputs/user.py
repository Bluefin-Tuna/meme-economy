import graphene

class CreateUserInput(graphene.InputObjectType):

    email = graphene.String(required = True)
    username = graphene.String(required = True)
    password = graphene.String(required = True)
    first_name = graphene.String(required = True)
    last_name = graphene.String(required = True)

class UpdateUserInput(graphene.InputObjectType):
    
    id = graphene.ID(required = True)

    email = graphene.String()
    username = graphene.String()
    password = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()

class DeleteUserInput(graphene.InputObjectType):

    id = graphene.ID(required = True)