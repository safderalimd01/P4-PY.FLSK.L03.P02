# ~/mysql-flask-connector/resources/inventory/inv_routes.py

# Product
from .products import ClsProduct
from .productList import ClsProductList


def initialize_product_routes(api):
    api.add_resource(ClsProduct, '/api/product')
    api.add_resource(ClsProductList, '/api/product-list')
