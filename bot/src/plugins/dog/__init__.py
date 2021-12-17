from re import findall
from random import choice
import os

from nonebot.typing import T_State
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, MessageEvent, GroupMessageEvent
from nonebot.adapters.cqhttp.permission import GROUP_OWNER, GROUP_ADMIN


from .data_source import Dog


dog = Dog().on_command("妈的有狗", "新增狗币",permission=SUPERUSER)


@dog.args_parser  # type: ignore
async def _dog(bot: Bot, event: MessageEvent, state: T_State):
    msg = str(event.message).strip()
    quit_list = ["算了", "罢了"]
    if msg in quit_list:
        await dog.finish("好吧...")
    if not msg:
        await dog.reject("是谁？")
    else:
        state["d"] = msg


@dog.handle()
async def _ready_add(bot: Bot, event: MessageEvent, state: T_State):
    # user_id = event.get_user_id()
    # if not _search_flmt.check(user_id):
    #     await addquery.finish(_search_flmt_notice)

    msg = str(event.message).strip()
    if msg:
        state["d"] = msg


@dog.got("d", "是谁？")
async def _deal_add(bot: Bot, event: MessageEvent, state: T_State):
    # user_id = event.get_user_id()
    
    try:
        msg = str(state["d"])
        if not msg:
            await dog.finish("捏麻麻的麻利点")
        a = Dog()
        code,result = await a.add(msg)
        await dog.finish(Message(result))
    except Exception as e:
        print('**************************************')
        print(e)
        print('**************************************')


qdog = Dog().on_command("看看狗托", "查询狗币")

@qdog.args_parser  # type: ignore
async def _qdog(bot: Bot, event: MessageEvent, state: T_State):
    msg = str(event.message).strip()
    quit_list = ["算了", "罢了"]
    if msg in quit_list:
        await qdog.finish("好吧...")
    if not msg:
        await qdog.reject("查谁？")
    else:
        state["d"] = msg


@qdog.handle()
async def _ready_q(bot: Bot, event: MessageEvent, state: T_State):
    # user_id = event.get_user_id()
    # if not _search_flmt.check(user_id):
    #     await addquery.finish(_search_flmt_notice)

    msg = str(event.message).strip()
    if msg:
        state["d"] = msg


@qdog.got("d", "是谁？")
async def _deal_q(bot: Bot, event: MessageEvent, state: T_State):
    # user_id = event.get_user_id()
    
    try:
        msg = str(state["d"])
        if not msg:
            await qdog.finish("捏麻麻的麻利点")
        a = Dog()
        code,result = await a.query(msg)
        await qdog.finish(Message(result))
    except Exception as e:
        print('**************************************')
        print(e)
        print('**************************************')