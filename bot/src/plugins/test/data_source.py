import base64

# from pathlib import Path
from random import choice
from nonebot.adapters.cqhttp import MessageSegment
from src.models import DBSession,PICS,RAID

from src.service import Service
from src.rule import is_in_service



class Test(Service):
    def __init__(self):
        Service.__init__(self, "test", "cs", rule=is_in_service("test"))

    @staticmethod
    async def t1():
        pass