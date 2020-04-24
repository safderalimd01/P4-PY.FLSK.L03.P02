from flask_restful import Resource
from flask import request

from resources.utility.config import connect_db
from resources.utility.utils import api_success, api_failure, close_connection


class ClsClient(Resource):

    def get(self):
        try:
            conn = connect_db()
            client_id = int(request.headers.get('client_id'))
            if not isinstance(conn, str):
                cursor = conn.cursor(dictionary=True)
                query = "SELECT client_id, client_name, client_status, mobile_phone, email_address, city FROM client \
                         WHERE client_id = {client_id}".format(client_id = client_id)
                cursor.execute(query)
                clientRow = cursor.fetchone()
                close_connection(conn, cursor)

                return api_success(clientRow, "Client details fetched successfully")
            else:
                return api_failure(str(conn))
        except Exception as error:
            return api_failure(str(error))


    def post(self):
        try:
            conn = connect_db()
            _json = request.json
            _client_name = _json['client_name']
            _client_status = _json['client_status']
            _mobile_phone = _json['mobile_phone']
            _email_address = _json['email_address']
            _city = _json['city']
            if not isinstance(conn, str):
                cursor = conn.cursor(dictionary=True)
                query = "INSERT INTO client(client_name, client_status, mobile_phone, email_address, city) VALUES(%s, %s, %s, %s, %s)"
                bindData = (_client_name, _client_status, _mobile_phone, _email_address, _city)
                cursor = conn.cursor()
                cursor.execute(query, bindData)
                conn.commit()
                close_connection(conn, cursor)

                return api_success(None, "Client saved successfully")
            else:
                return api_failure(str(conn))
        except Exception as error:
            return api_failure(str(error))


    def put(self):
        try:
            conn = connect_db()
            _json = request.json
            _client_id = _json['client_id']
            _client_name = _json['client_name']
            _client_status = _json['client_status']
            _mobile_phone = _json['mobile_phone']
            _email_address = _json['email_address']
            _city = _json['city']
            if not isinstance(conn, str):
                cursor = conn.cursor(dictionary=True)
                query = "UPDATE client set client_name=%s, client_status=%s, mobile_phone=%s, email_address=%s, city=%s where client_id = %s"
                bindData = (_client_name, _client_status, _mobile_phone, _email_address, _city, _client_id)
                cursor = conn.cursor()
                cursor.execute(query, bindData)
                conn.commit()
                close_connection(conn, cursor)

                return api_success(None, "Client updated successfully")
            else:
                return api_failure(str(conn))
        except Exception as error:
            return api_failure(str(error))


    def delete(self):
        try:
            conn = connect_db()
            _client_id = int(request.headers.get('client_id'))
            if not isinstance(conn, str):
                cursor = conn.cursor(dictionary=True)
                query = "DELETE FROM client WHERE client_id =%s"
                bindData = (_client_id, )
                cursor.execute(query, bindData)
                conn.commit()
                close_connection(conn, cursor)

                return api_success(None, "Client deleted successfully")
            else:
                return api_failure(str(conn))
        except Exception as error:
            return api_failure(str(error))
