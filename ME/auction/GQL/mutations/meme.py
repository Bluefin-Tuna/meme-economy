import graphene
from auction.GQL.inputs.meme import CreateMemeInput, UpdateMemeInput, DeleteMemeInput
from core.models import Profile
from auction.models import Meme
from auction.GQL.types import MemeType


class CreateMeme(graphene.Mutation):

    class Arguments:
        information = CreateMemeInput(required = True)

    meme = graphene.Field(MemeType)

    @staticmethod
    def mutate(root, info, information = None):
        
        owner = Profile.objects.get(id = information.owner)
        meme = Meme(
            owner = owner,
            name = information.name,
            description = information,
            file = information.file,
        )
        meme.save()

        return CreateMeme(meme = meme)


class UpdateMeme(graphene.Mutation):

    class Arguments: 
        information = UpdateMemeInput(required = True)
    
    meme = graphene.Field(MemeType)

    @staticmethod
    def mutate(root, info, information = None):
        
        meme = Meme.objects.get(id = information.id)

        if(meme):

            for key in information:
                exec(f'meme.{key} = information.{key}')
            meme.save()

            return UpdateMeme(meme = meme)
        
        return UpdateMeme(meme = None)


class DeleteMeme(graphene.Mutation):

    class Arguments:
        information = DeleteMemeInput(required = True)

    meme = graphene.Field(MemeType)

    @staticmethod
    def mutate(root, info, information = None):

        meme = Meme.objects.get(id = information.id)
        meme.delete()

        return None



class MemeMutation(graphene.ObjectType):

    create_meme = CreateMeme.Field()
    update_meme = UpdateMeme.Field()
    delete_meme = DeleteMeme.Field()