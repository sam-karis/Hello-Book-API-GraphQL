from flask import Flask
from flask_graphql import GraphQLView
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from api.database import db_session
from schema import schema
from config import config
from helpers.auth.auth_request import AuthRequest

db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    app.config['JWT_SECRET_KEY'] = 'jwt-token-secret-key'
    config[config_name].init_app(app)
    db.init_app(app)
    jwt = JWTManager(app)

    app.add_url_rule(
        '/hblms',
        view_func=GraphQLView.as_view(
            'hblms',
            schema=schema,
            graphiql=True  # for having the GraphiQL interface
        )
    )

    @app.route("/auth", methods=['POST'])
    def authenticate_user():
        return AuthRequest.validate_request(AuthRequest)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    return app
