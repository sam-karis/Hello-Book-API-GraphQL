from graphql import GraphQLError

class ErrorHandler():
    '''Handles error'''

    def check_conflict(self, model_param, description):
        # Database integrity error
        raise GraphQLError(
            '{} {} already exists'.format(model_param, description))

    def foreign_key_conflict(self, model_param, description):
        # Database foreign key error
        raise GraphQLError(
            '{} {} does not exists'.format(model_param, description))

    def db_connection(self):
        # Database connection error
        raise GraphQLError('Error: Could not connect to Db')