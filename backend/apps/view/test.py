from flask_restful import Resource, reqparse
from flask import abort
from flask_jwt_extended import jwt_required,get_jwt_identity


class test(Resource):
    @jwt_required()
    def get(self):
        print(get_jwt_identity())
        abort(404,'做乜啦')
    def post(self):
        return 'well,post'
    def put(self):
        return 'well,put'
    def delete(self):
        return 'well,del'