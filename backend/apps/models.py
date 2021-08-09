#encoding:utf-8

# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column,Integer,String,ForeignKey,SmallInteger,Date
# from sqlalchemy.orm import sessionmaker, scoped_session
from ext import db
import bcrypt
import time
import hashlib
import config


class User(db.Model):
    __tablename__ = 'user'

    username = db.Column(db.String(255),primary_key=True,nullable=False)
    userpwd = db.Column(db.String(255),nullable=False)
    auth = db.Column(db.String(255),nullable=False)

    def check_pwd(self, raw_pwd):
        if bcrypt.checkpw(raw_pwd.encode('utf-8'), self.userpwd.encode('utf-8')):
            return True
        else:
            return False


    def set_pwd(self, raw_pwd):
        self.userpwd = bcrypt.hashpw(raw_pwd.encode('utf-8'), bcrypt.gensalt())
        return True

    def modify_pwd(self, raw_pwd, new_pwd):
        if self.check_pwd(raw_pwd):
            self.set_pwd(new_pwd)
            return True
        else:
            return False

    def __repr__(self):
        return self.username
