from flask_restful import Resource
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, create_refresh_token,
    get_jwt_identity,decode_token,get_jwt
)
from flask import request,abort
from datetime import datetime,timedelta
from apps.models import *

import json


class Login(Resource):
    def post(self):
        try:
            data = json.loads(request.get_data().decode("utf-8"))
            username = data['username']
            userpwd = data['password']
            user = User.query.filter_by(username=username).one()
            if user.check_pwd(userpwd):
                access_token = create_access_token(
                    identity=username,
                    expires_delta = timedelta(seconds=36000),
                    additional_claims={"auth":user.auth},
                    fresh=True)
                refresh_token = create_refresh_token(identity=username,additional_claims={"auth":user.auth})
                return {
                        'code':20000,
                        'access_token': access_token,
                        'refresh_token': refresh_token
                    }, 200
            else:
                return {"message": "Invalid Credentials."}, 401
        except Exception as e:
            print(e)
            abort(500)
            

class TokenRefresh(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        jwt = get_jwt()
        new_token = create_access_token(identity=current_user,additional_claims={"auth":jwt['auth']}, fresh=False)
        return {'access_token': new_token}, 200


class GetUserInfo(Resource):
    @jwt_required()
    def get(self):
        jwt = get_jwt()
        current_user = get_jwt_identity()
        return {'roles': jwt['auth'], 'name': current_user}, 200


class LogOut(Resource):
    @jwt_required()
    def post(self):
        return 'done', 200