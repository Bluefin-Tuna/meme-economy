import graphene
from core.GQL.mutations.user import UserMutation
from core.GQL.mutations.profile import ProfileMutation

class CoreMutations(UserMutation, ProfileMutation, graphene.ObjectType):
    pass