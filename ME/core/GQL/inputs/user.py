import graphene
from graphene_file_upload.scalars import Upload

class UserInput(graphene.InputObjectType):

    email = graphene.String(required = True)
    username = graphene.String(required = True)
    password = graphene.String(required = True)
    first_name = graphene.String(required = True)
    last_name = graphene.String(required = True)