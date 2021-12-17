from random import choice
from aiohttp import FormData


from src.service import Service
from src.rule import is_in_service


from sqlalchemy.orm import sessionmaker
from src.models import DBSession,DOG


import time
import urllib

__doc__ = """
添加图片！自定义查询！
"""


class Dog(Service):
    def __init__(self):
        Service.__init__(self, "查询狗币", __doc__, rule=is_in_service("查询狗币"))

    async def add(self, name):
        try:
            dbsession = DBSession()
            try:
                # print(name)
                result = dbsession.query(DOG).filter(DOG.name==str(name)).one()
                result.num+=1
                dbsession.commit()
                ret=result.num
                dbsession.close()
                return 200,'顺带一提，这是'+str(name)+'第'+str(ret)+'次当狗'
            except Exception as e:
                result = DOG(name = name, num = 1)
                dbsession.add(result)
                dbsession.commit()
                dbsession.close()
                return 200, '顺带一提，这是'+str(name)+'第一次当狗'
        except Exception as e:
            print(e)
            return 500,'出错啦'

    async def query(self, name):
        try:
            dbsession = DBSession()
            try:
                result = dbsession.query(DOG).filter(DOG.name==str(name)).one()
                dbsession.close()
                return 200,str(name)+'已经狗了'+str(result.num)+'次了'
            except Exception as e:
                dbsession.close()
                return 404,str(name)+'还没狗过'
        except Exception as e:
            print(e)
            return 500,'出错啦'

