#encoding:utf-8

from flask_restful import Api
from .view.test import test
from .view.user import Login

api = Api(prefix='/api/v1')
api.add_resource(test,'/test')
api.add_resource(Login,'/login')