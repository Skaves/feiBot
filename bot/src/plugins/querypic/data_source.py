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


class Querypic(Service):
    def __init__(self):
        Service.__init__(self, "查找图片", __doc__, rule=is_in_service("查找图片"))


    async def query(self, name):
        try:
            dbsession = DBSession()
            try:
                # print(name)
                result = dbsession.query(PICS).filter(PICS.name==str(name)).one()
                ret=result.path
                # print(ret)
                # filename = './pics/{}'.format(result.path)
                dbsession.close()
                return 200,ret
            except Exception as e:
                print(e)
                dbsession.close()
                return 404,'没找着'
        except Exception as e:
            print(e)
            return 500,'出错啦'

