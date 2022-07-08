import graphene
from ME.core.models import User
from ME.core.GQL.inputs.user import CreateUserInput, DeleteUserInput, UpdateUserInput
from ME.core.GQL.types import UserType

class CreateUser(graphene.Mutation):

    class Arguments:
        information = CreateUserInput(required = True)
    
    user = UserType()

    @staticmethod
    def mutate(root, info, information = None):

        user = User(
            email = information.email,
            username = information.username,
            password = information.password,
            first_name = information.first_name,
            last_name = information.last_name,
        )
        user.save()

        return CreateUser(user = user)

class UpdateUser(graphene.Mutation):

    class Arguments:
        information = UpdateUserInput(required = True)
    
    user = UserType()

    @staticmethod
    def mutate(root, info, information = None):
        
        user = User.objects.get(id = information.id)

        if(user):

            for key in information:
                exec(f'user.{key} = information.{key}')
            user.save()

            return UpdateUser(user = user)
        
        return UpdateUser(user = None)

class DeleteUser(graphene.Mutation):

    class Arguments:
        information = DeleteUserInput(required = True)
    
    user = UserType()

    @staticmethod
    def mutate(root, info, information = None):

        user = User.objects.get(id = information.id)
        user.delete()

        return None