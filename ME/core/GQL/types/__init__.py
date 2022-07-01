from graphene_django import DjangoObjectType
from core.models import User, Profile

class UserType(DjangoObjectType):
    
    class Meta:
        model = User
        exclude = ("password",)


class ProfileType(DjangoObjectType):

    class Meta:
        model = Profile
        fields = "__all__"