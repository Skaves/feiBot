from flask_restful import Resource
from flask_jwt_extended import create_access_token,create_refresh_token
from flask import request
from apps.models import *

import json


class Login(Resource):
    def post(self):
        try:
            data = json.loads(request.get_data().decode("utf-8"))
            username = data['username']
            userpwd = data['userpwd']
            user = User.query.filter_by(username=username).one()
            if user.check_pwd(userpwd):
                access_token = create_access_token(
                    identity=username,
                    additional_claims={"auth":user.auth},
                    fresh=True)
                refresh_token = create_refresh_token(username)
                return {
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    }, 200
            else:
                return {"message": "Invalid Credentials."}, 401
        except Exception as e:
            print(e)
            abort(401)
            