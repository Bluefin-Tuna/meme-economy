import graphene
from graphene_file_upload.scalars import Upload

class ProfileInput(graphene.InputObjectType):
    
    user = graphene.ID(required = True)
    assets = graphene.Int()
    profile_picture = Upload(required = True)