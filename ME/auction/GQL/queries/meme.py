import graphene
from auction.models import Meme
from auction.GQL.types import MemeType

class MemeQueries(graphene.ObjectType):

    all_memes = graphene.List(MemeType)
    meme = graphene.Field(MemeType, id = graphene.Int)

    def resolve_all_memes(self, info, **kwargs):
        return Meme.objects.get()
    
    def resolve_meme(self, info, id):
        return Meme.objects.get(id = id)