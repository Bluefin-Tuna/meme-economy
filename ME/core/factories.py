import random
import factory
from factory.django import DjangoModelFactory

from core.models import *

class UserFactory(DjangoModelFactory):

    class Meta:
        model = User
    
    email = factory.Faker("email")
    username = factory.Faker("user_name")
    password = factory.Faker("password")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")

    profile = factory.RelatedFactory(
        "core.factories.ProfileFactory", 
        factory_related_name = "user",
    )


class ProfileFactory(DjangoModelFactory):

    class Meta:
        model = Profile
    
    assets = random.randint(0, 10000)
    profile_picture = factory.django.ImageField(color = "blue")
    
    user = factory.SubFactory(
        "core.factories.UserFactory", 
        profile = None,
    )