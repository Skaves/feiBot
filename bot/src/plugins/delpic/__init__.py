from re import findall
from random import choice

from nonebot.typing import T_State
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, MessageEvent, GroupMessageEvent
from nonebot.adapters.cqhttp.permission import GROUP_OWNER, GROUP_ADMIN
# from sec.config import SauceNAO
from src.utils.limit import FreqLimiter
from .data_source import Delpic


_search_flmt = FreqLimiter(10)
_search_flmt_notice = choice(["慢...慢一..点❤", "冷静1下", "歇会歇会~~"])


delpic = Delpic().on_command("删除图片", "从数据库删除一张图片", permission=SUPERUSER)


@delpic.args_parser  # type: ignore
async def _get_img(bot: Bot, event: MessageEvent, state: T_State):
    msg = str(event.message).strip()
    quit_list = ["算了", "罢了", "不加了"]
    if msg in quit_list:
        await delpic.finish("好吧...")
    if not msg:
        await delpic.reject("给个关键词？")
    else:
        state["img"] = msg


@delpic.handle()
async def _ready_add(bot: Bot, event: MessageEvent, state: T_State):
    # user_id = event.get_user_id()
    # if not _search_flmt.check(user_id):
    #     await addquery.finish(_search_flmt_notice)

    msg = str(event.message).strip()
    if msg:
        state["img"] = msg


@delpic.got("img", "图呢？")
async def _deal_add(bot: Bot, event: MessageEvent, state: T_State):
    # user_id = event.get_user_id()
    
    try:
        msg = str(state["img"])
        if not msg:
            await delpic.finish("捏麻麻的麻利点")
        a = Delpic()
        result = await a.dele(msg)
        await delpic.finish(result)
    except Exception as e:
        print('**************************************')
        print(e)
        print('**************************************')
        # await addpic.finish("图和关键词不能一起发？")
