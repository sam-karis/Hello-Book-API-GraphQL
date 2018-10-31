import graphene
from graphene_sqlalchemy import (SQLAlchemyObjectType)

import api.user.schema

class Query(api.user.schema.Query):
    pass


class Mutation(api.user.schema.Mutation):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
