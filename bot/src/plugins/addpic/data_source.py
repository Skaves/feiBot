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


class Addpic(Service):
    def __init__(self):
        Service.__init__(self, "添加图片", __doc__, rule=is_in_service("添加图片"))


    async def add(self, name, url):
        try:
            dbsession = DBSession()
            try:
                result = dbsession.query(PICS).filter(PICS.name==str(name)).one()
                dbsession.close()
                return '关键词重复'
            except:
                name = name.replace('\r','').replace('\n','')
                t = time.time()
                fn = str(int(round(t * 1000000)))+'.jpg'
                fname = './pics/'+fn
                urllib.request.urlretrieve(url, filename=fname)
                data = PICS(name=str(name),path=fn)
                dbsession.add(data)
                dbsession.commit()
                dbsession.close()
                return '搞定'
        except Exception as e:
            print(e)
            return '出错啦'

