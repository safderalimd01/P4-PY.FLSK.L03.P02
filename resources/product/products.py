from flask_restful import Resource
from flask import request

from resources.utility.config import connect_db
from resources.utility.utils import api_success, api_failure, close_connection


class ClsProduct(Resource):

    def get(self):
        try:
            conn = connect_db()
            product_id = int(request.headers.get('product_id'))
            if not isinstance(conn, str):
                cursor = conn.cursor(dictionary=True)
                query = "SELECT product_id, product_name, product_status FROM product \
                         WHERE product_id = {product_id}".format(product_id = product_id)
                cursor.execute(query)
                productRow = cursor.fetchone()
                close_connection(conn, cursor)

                return api_success(productRow, "Products details fetched successfully")
            else:
                return api_failure(str(conn))
        except Exception as error:
            return api_failure(str(error))


    def post(self):
        try:
            conn = connect_db()
            _json = request.json
            _product_name = _json['product_name']
            _product_status = _json['product_status']
            if not isinstance(conn, str):
                cursor = conn.cursor(dictionary=True)
                query = "INSERT INTO product(product_name, product_status) VALUES(%s, %s)"
                bindData = (_product_name, _product_status)
                cursor = conn.cursor()
                cursor.execute(query, bindData)
                conn.commit()
                close_connection(conn, cursor)

                return api_success(None, "Product saved successfully")
            else:
                return api_failure(str(conn))
        except Exception as error:
            return api_failure(str(error))


    def put(self):
        try:
            conn = connect_db()
            _json = request.json
            _product_id = _json['product_id']
            _product_name = _json['product_name']
            _product_status = _json['product_status']
            if not isinstance(conn, str):
                cursor = conn.cursor(dictionary=True)
                query = "UPDATE product set product_name=%s, product_status=%s where product_id = %s"
                bindData = (_product_name, _product_status, _product_id)
                cursor = conn.cursor()
                cursor.execute(query, bindData)
                conn.commit()
                close_connection(conn, cursor)

                return api_success(None, "Product updated successfully")
            else:
                return api_failure(str(conn))
        except Exception as error:
            return api_failure(str(error))


    def delete(self):
        try:
            conn = connect_db()
            _product_id = int(request.headers.get('product_id'))
            if not isinstance(conn, str):
                cursor = conn.cursor(dictionary=True)
                query = "DELETE FROM product WHERE product_id =%s"
                bindData = (_product_id, )
                cursor.execute(query, bindData)
                conn.commit()
                close_connection(conn, cursor)

                return api_success(None, "Products deleted successfully")
            else:
                return api_failure(str(conn))
        except Exception as error:
            return api_failure(str(error))
