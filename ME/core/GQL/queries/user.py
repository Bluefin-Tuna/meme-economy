from django.shortcuts import get_object_or_404
import graphene
from core.models import User
from core.GQL.types import UserType

class UserQuery(graphene.ObjectType):

    all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id = graphene.Int())
    sign_in = graphene.Field(UserType, username = graphene.String(), password = graphene.String())

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()
    
    def resolve_user(self, info, id):
        return User.objects.get(id = id)
    
    def resolve_signin(self, info, username, password):
        return get_object_or_404(User, username = username, password = password)