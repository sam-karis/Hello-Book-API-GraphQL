from flask import request, jsonify
from flask_json import JsonError
from flask_jwt_extended import create_access_token

from api.user.models import User


class AuthRequest():
    """
    Handle user authentication requests
    """
    def validate_request(self):
        '''
        Validate request
        '''
        request_data = request.get_json()
        required_params = ('username', 'password')
        if not all(param in request_data for param in required_params):  # noqa: E501
            return jsonify(
                {"Error": "Request must have username and password"}
            ), 400
        return AuthRequest.get_user_data(self, request_data)
    
    def generate_access_token(self, username):
        '''
        Generate access token
        '''
        token = create_access_token(identity=username)
        return token

    def get_user_data(self, user_data):
        '''
        Get user data from db
        '''
        user= User.query.filter_by(username=user_data['username']).first()
        if user:
            if user.check_password(user_data['password']):
                token = AuthRequest.generate_access_token(self, user_data['username'])
                response = jsonify({"access_token": token})
            else:
                response = jsonify({"Error": 'Invalid password or username'}), 401
        else:
            response = jsonify({"Error": 'Invalid password or username'}), 401
        return response
