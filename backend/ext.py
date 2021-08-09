#encoding:utf-8

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_jwt_extended import JWTManager

csrf = CSRFProtect()
db = SQLAlchemy()
jwt = JWTManager()


