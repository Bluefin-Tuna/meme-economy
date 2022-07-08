import graphene
from graphene_file_upload.scalars import Upload

class CreateProfileInput(graphene.InputObjectType):
    
    user = graphene.ID(required = True)
    profile_picture = Upload(required = True)

class UpdateProfileInput(graphene.InputObjectType):
    