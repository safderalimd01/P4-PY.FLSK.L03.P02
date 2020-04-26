# Product
from .login import ClsLogin


def initialize_auth_routes(api):
    api.add_resource(ClsLogin, '/api/login')
