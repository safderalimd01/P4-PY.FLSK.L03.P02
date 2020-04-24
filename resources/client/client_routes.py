# ~/mysql-flask-connector/resources/inventory/inv_routes.py

# Product
from .clients import ClsClient
from .clientList import ClsClientList


def initialize_client_routes(api):
    api.add_resource(ClsClient, '/api/client')
    api.add_resource(ClsClientList, '/api/client-list')
