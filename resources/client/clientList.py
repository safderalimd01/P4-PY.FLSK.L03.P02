from flask_restful import Resource
from flask import request

from resources.utility.config import connect_db
from resources.utility.utils import api_success, api_failure, close_connection

import os
import mysql.connector

config = {
    'user': os.environ.get('user'),
    'password': os.environ.get('password'),
    'host': os.environ.get('host'),
    'database': os.environ.get('database')
}

class ClsClientList(Resource):

    def get(self):
        try:
            conn = mysql.connector.connect(**config)
            if not isinstance(conn, str):
                cursor = conn.cursor(dictionary=True)
                cursor.execute("SELECT client_id, client_name, mobile_phone, email_address, city FROM client")
                clientRows = cursor.fetchall()
                close_connection(conn, cursor)

                results = []
                for result in clientRows:
                    results.append(result)

                return api_success(results, "Clients lists fetched successfully")
            else:
                return api_failure(str(conn))
        except Exception as error:
            return api_failure(str(error))
