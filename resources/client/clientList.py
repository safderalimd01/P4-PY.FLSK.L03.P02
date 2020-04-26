from flask_restful import Resource
from flask import request

from resources.utility.config import db_connect
from resources.utility.utils import api_success, api_failure, close_connection
from flask_jwt_extended import jwt_required


class ClsClientList(Resource):

    @jwt_required
    def get(self):
        try:
            db = db_connect()
            conn = db.connect()
            cursor = conn.cursor()

            if not isinstance(conn, str):
                cursor.execute("SELECT client_id, client_name, mobile_phone, email_address, city FROM client")
                clientRows = cursor.fetchall()
                close_connection(conn, cursor)
                return api_success(clientRows, "Clients lists fetched successfully")
            else:
                return api_failure(str(conn))
        except Exception as error:
            return api_failure(str(error))
