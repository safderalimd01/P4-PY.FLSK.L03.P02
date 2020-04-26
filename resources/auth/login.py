from flask import Flask, request
from flask_restful import Resource

import os

from resources.utility.config import app, db_connect
from werkzeug.security import safe_str_cmp

from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import jwt_required

app.secret_key = 'https://wwww.tansycloud.com'
jwt = JWTManager(app)


class ClsLogin(Resource):

    def post(self, *args, **kwargs):
        _json = request.json
        _username = _json.get('username', None)
        _password = _json.get('password', None)

        try:
            res = db_connect()
            conn = res.connect()
            cursor = conn.cursor()

            cursor.execute("SELECT id, username, password FROM user")
            db_users = cursor.fetchall()

            username_table = {u.get('username', None): u for u in db_users}
            userid_table = {u.get('id', None): u for u in db_users}

            user = username_table.get(_username, None)
            if user and safe_str_cmp(user.get('password'), _password):
                access_token = create_access_token(identity=user.get('username'))
                return {
                    'access_token': access_token
                }, 200

            return {"message": "Invalid Credentials!"}, 401
        except Exception as e:
            return {"message": str(e)}, 400
