#encoding:utf-8

from flask_restful import Api
from .view.test import test
from .view.user import Login,TokenRefresh,GetUserInfo,LogOut

api = Api(prefix='/api/v1')
api.add_resource(test,'/test')
api.add_resource(Login,'/login')
api.add_resource(GetUserInfo,'/userinfo')
api.add_resource(LogOut,'/logout')
api.add_resource(TokenRefresh,'/refresh')