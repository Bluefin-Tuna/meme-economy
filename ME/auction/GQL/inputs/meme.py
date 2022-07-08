import graphene
from graphene_file_upload.scalars import Upload

class CreateMemeInput(graphene.InputObjectType):

    owner = graphene.ID(required = True)
    
    name = graphene.String(required = True)
    description = graphene.String()
    file = Upload(required = True)


class UpdateMemeInput(graphene.InputObjectType):

    id = graphene.ID(required = True)

    owner = graphene.ID()
    auction = graphene.ID()
    name = graphene.String()
    description = graphene.String()

class DeleteMemeInput(graphene.InputObjectType):

    id = graphene.ID(required = True)