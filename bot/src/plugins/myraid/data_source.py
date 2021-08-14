import base64

# from pathlib import Path
from random import choice
from nonebot.adapters.cqhttp import MessageSegment
from src.models import DBSession,PICS,RAID

from src.service import Service
from src.rule import is_in_service



class myTuan(Service):
    def __init__(self):
        Service.__init__(self, "我的团", "gkd!", rule=is_in_service("我的团"))


    @staticmethod
    async def allwave(wv):
        """
        发指自己的安排.
        """
        res = -1
        dbsession = DBSession()
        try:
            res = dbsession.query(RAID).filter(RAID.qq==wv).all()
        except Exception as e:
            print(e)
        dbsession.close()
        return res