import base64

# from pathlib import Path
from random import choice
from nonebot.adapters.cqhttp import MessageSegment
from src.models import DBSession,PICS,RAID

from src.service import Service
from src.rule import is_in_service



class Tuan(Service):
    def __init__(self):
        Service.__init__(self, "开团", "gkd!", rule=is_in_service("开团"))

    @staticmethod
    async def totaltable() -> tuple:
        """
        发总表.
        """
        ret = -1
        dbsession = DBSession()
        try:
            pic = dbsession.query(PICS).filter(PICS.name=='攻坚表').one()
            ret = pic.path
        except Exception as e:
            print(e)
        dbsession.close()
        return ret

    @staticmethod
    async def singlewave(wv):
        """
        发指定波名单.
        """
        res = -1
        dbsession = DBSession()
        try:
            res = dbsession.query(RAID).filter(RAID.wave==str(wv)).all()
        except Exception as e:
            print(e)
        dbsession.close()
        return res