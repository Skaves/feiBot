import re
import asyncio
import os
from random import choice
from nonebot.adapters.cqhttp import Bot, MessageEvent,Message,MessageSegment,GroupMessageEvent
from nonebot.adapters.cqhttp import GROUP_ADMIN, GROUP_OWNER
from nonebot.permission import SUPERUSER

from .data_source import Test


test = Test().on_command(
    "test",  "测试", permission=SUPERUSER
)


@test.handle()
async def _test(bot: Bot, event: GroupMessageEvent):
    group_id = event.group_id
    user_id = event.get_user_id()
    prep_list = await bot.get_group_member_list(group_id=group_id)
    mp = {}
    for i in prep_list:
        mp[i['nickname']]=i['user_id']
    # info: dict = await bot.get_group_member_info(
    #     group_id=group_id, user_id=int(user_id)
    # )
    print(mp)
    await test.finish('Done.请查看控制台.')
