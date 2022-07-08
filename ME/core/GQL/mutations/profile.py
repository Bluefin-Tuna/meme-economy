import graphene

from ME.core.GQL.inputs.profile import CreateProfileInput, UpdateProfileInput
from ME.core.GQL.types import ProfileType
from ME.core.models import Profile, User

class CreateProfile(graphene.Mutation):

    class Arguments:
        information = CreateProfileInput(required = True)
    
    profile = ProfileType()

    @staticmethod
    def mutate(root, info, information = None):

        user = User.objects.get(id = information.user)
        
        profile = Profile(user = user,)
        if(hasattr(information, "profile_picture")):
            profile.profile_picture = information.profile_picture
        profile.save()

        return CreateProfile(profile = profile)

class UpdateProfile(graphene.Mutation):

    class Arguments:
        information = UpdateProfileInput(required = True)
    
    profile = ProfileType()

    @staticmethod
    def mutate(root, info, information = None):

        profile = Profile.objects.get(id = information.id)

        if(profile):

            for key in information:
                exec(f'profile.{key} = information.{key}')
            profile.save()

            return UpdateProfile(profile = profile)
        
        return UpdateProfile(profile = None)