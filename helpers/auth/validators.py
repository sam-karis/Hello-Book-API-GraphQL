from graphql import GraphQLError
import re


def verify_email(email):
    valid = re.match(
        "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
    if valid is None:
        raise GraphQLError('Use a valid email')
    pass

def validate_password(password):
    required_pattern = re.compile('(?=.{6,})(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])')
    valid = required_pattern.match(password)
    if valid is None:
        raise GraphQLError('Valid password must have atleast one uppercase, lowercase, and a digit')
    return valid
