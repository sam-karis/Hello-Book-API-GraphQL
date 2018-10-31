import graphene
from graphene_sqlalchemy import (SQLAlchemyObjectType)
from graphql import GraphQLError

from api.user.models import User as UserModel
from helpers.context_manager import SaveContextManager
from helpers.auth.validators import verify_email, validate_password


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        query = User.get_query(info)
        return query.all()

class RegisterUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        name = graphene.String(required=False)
        username = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(User)

    def mutate(self, info, **kwargs):
        verify_email(kwargs['email'])
        validate_password(kwargs['password'])
        new_user = UserModel(name=kwargs['name'], email=kwargs['email'], username=kwargs['username'])
        new_user.hash_password(kwargs['password'])
        with SaveContextManager(new_user, kwargs.get('username'), 'username or email'):
            return RegisterUser(user=new_user)


class Mutation(graphene.ObjectType):
    register_user = RegisterUser.Field()