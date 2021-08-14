import re
import asyncio
import os
from random import choice
from nonebot.adapters.cqhttp import Bot, MessageEvent,Message,MessageSegment

from .data_source import myTuan


kantuan = myTuan().on_command(
    "看看我的攻坚安排",  "发言者的攻坚表", aliases={"我怎么安排"}
)


@kantuan.handle()
async def _kantuan(bot: Bot, event: MessageEvent):
    user_id = event.get_user_id()
    li = await myTuan.allwave(user_id)
    ret = f"{MessageSegment.at(user_id)}"+"你的安排是："
    for i in li:
        ret += "第"+str(i.wave)+"波"+i.team+"队"+"来"+str(i.role)+"   "
    await kantuan.finish(Message(ret))
