import graphene
from core.models import Profile
from core.GQL.types import ProfileType

class ProfileQueries(graphene.ObjectType):

    profile = graphene.Field(ProfileType, id = graphene.Int)

    def resolve_profile(self, info, id):
        return Profile.objects.get(id = id)