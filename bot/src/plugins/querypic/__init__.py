from re import findall
from random import choice
import os

from nonebot.typing import T_State
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, MessageEvent, GroupMessageEvent
from nonebot.adapters.cqhttp.permission import GROUP_OWNER, GROUP_ADMIN


from .data_source import Querypic


querypic = Querypic().on_command("查询图片", "查询数据库中的图片", aliases={"查图","查询"})


@querypic.args_parser  # type: ignore
async def _get_img(bot: Bot, event: MessageEvent, state: T_State):
    msg = str(event.message).strip()
    quit_list = ["算了", "罢了", "不加了"]
    if msg in quit_list:
        await querypic.finish("好吧...")
    if not msg:
        await querypic.reject("查啥啊？")
    else:
        state["img"] = msg


@querypic.handle()
async def _ready_add(bot: Bot, event: MessageEvent, state: T_State):
    # user_id = event.get_user_id()
    # if not _search_flmt.check(user_id):
    #     await addquery.finish(_search_flmt_notice)

    msg = str(event.message).strip()
    if msg:
        state["img"] = msg


@querypic.got("img", "查啥啊？")
async def _deal_add(bot: Bot, event: MessageEvent, state: T_State):
    # user_id = event.get_user_id()
    
    try:
        msg = str(state["img"])
        if not msg:
            await querypic.finish("捏麻麻的麻利点")
        a = Querypic()
        code,result = await a.query(msg)
        if code == 200:
            result = os.path.join(r'file:///D:/feiBot/bot/pics',result)
            ret = MessageSegment.image(result)
        else:
            ret=result
        await querypic.finish(Message(ret))
    except Exception as e:
        print('**************************************')
        print(e)
        print('**************************************')
