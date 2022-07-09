import graphene
from core.GQL.queries.user import UserQuery
from core.GQL.queries.profile import ProfileQuery

class CoreQueries(UserQuery, ProfileQuery, graphene.ObjectType):
    pass