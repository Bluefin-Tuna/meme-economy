import graphene

from core.GQL.inputs.profile import CreateProfileInput, UpdateProfileInput
from core.GQL.types import ProfileType
from core.models import Profile, User


class CreateProfile(graphene.Mutation):

    class Arguments:
        information = CreateProfileInput(required = True)
    
    profile = graphene.Field(ProfileType)

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
    
    profile = graphene.Field(ProfileType)

    @staticmethod
    def mutate(root, info, information = None):

        profile = Profile.objects.get(id = information.id)

        if(profile):

            for key in information:
                exec(f'profile.{key} = information.{key}')
            profile.save()

            return UpdateProfile(profile = profile)
        
        return UpdateProfile(profile = None)



class ProfileMutation(graphene.ObjectType):
    
    create_profile = CreateProfile.Field()
    update_profile = UpdateProfile.Field()