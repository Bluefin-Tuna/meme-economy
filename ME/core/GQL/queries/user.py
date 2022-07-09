import graphene
from core.models import User
from core.GQL.types import UserType

class UserQuery(graphene.ObjectType):

    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id = graphene.Int())

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()
    
    def resolve_user(self, info, id):
        return User.objects.get(id = id)