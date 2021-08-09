#encoding:utf-8
from flask import Flask,jsonify
import config
from ext import db,csrf,jwt
from apps.urls import api
from flask_cors import CORS

# from apps.msgCode import *


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    api.init_app(app)
    db.init_app(app)
    jwt.init_app(app)
    # register_errors(app)
    CORS(app)
    return app
