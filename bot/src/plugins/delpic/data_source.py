from random import choice
from aiohttp import FormData

from src.service import Service
from src.rule import is_in_service


from sqlalchemy.orm import sessionmaker
from src.models import DBSession,PICS


import time
import urllib

__doc__ = """
添加图片！自定义查询！
"""


class Delpic(Service):
    def __init__(self):
        Service.__init__(self, "删除图片", __doc__, rule=is_in_service("删除图片"))


    async def dele(self, name):
        try:
            dbsession = DBSession()
            try:
                dbsession.query(PICS).filter(PICS.name == name).delete()
                dbsession.commit()
                dbsession.close()
                return '搞定'
            except:
                dbsession.close()
                return '没有这个关键词'
        except Exception as e:
            print(e)
            return '出错啦'

