from re import findall
from random import choice

from nonebot.typing import T_State
from nonebot.adapters.cqhttp.message import Message, MessageSegment
from nonebot.permission import SUPERUSER
from nonebot.adapters.cqhttp import Bot, MessageEvent, GroupMessageEvent
from nonebot.adapters.cqhttp.permission import GROUP_OWNER, GROUP_ADMIN
# from sec.config import SauceNAO
from src.utils.limit import FreqLimiter
from .data_source import Addpic


_search_flmt = FreqLimiter(10)
_search_flmt_notice = choice(["慢...慢一..点❤", "冷静1下", "歇会歇会~~"])


addpic = Addpic().on_command("新增图片", "添加一张图片到数据库", aliases={"添加图片","增加图片"}, permission=SUPERUSER)


@addpic.args_parser  # type: ignore
async def _get_img(bot: Bot, event: MessageEvent, state: T_State):
    msg = str(event.message).strip()
    quit_list = ["算了", "罢了", "不加了"]
    if msg in quit_list:
        await addpic.finish("好吧...")
    if not msg:
        await addpic.reject("图呢？")
    else:
        state["img"] = msg


@addpic.handle()
async def _ready_add(bot: Bot, event: MessageEvent, state: T_State):
    # user_id = event.get_user_id()
    # if not _search_flmt.check(user_id):
    #     await addquery.finish(_search_flmt_notice)

    msg = str(event.message).strip()
    if msg:
        state["img"] = msg


@addpic.got("img", "图呢？")
async def _deal_add(bot: Bot, event: MessageEvent, state: T_State):
    # user_id = event.get_user_id()
    
    try:
        word = ''
        img = ''
        # 可能不分行的
        # test = str(state["img"]).split(r'\r\n')
        # print(test)
        msg = str(state["img"]).split(']')
        if msg[0][0]!='[':
            msg = str(state["img"]).split('[')
            img = findall(r"url=(.*?)]", '['+msg[1])
            word = msg[0]
        else:
            img = findall(r"url=(.*?)]", msg[0]+']')
            word = msg[1]
        if not img:
            await addpic.finish("捏麻麻的整张图！！")
        if not word:
            await addpic.finish("捏麻麻的关键词！！")
        # print(img)
        a = Addpic()
        # result = f"> {MessageSegment.at(user_id)}" + await a.add(img[0])
        result = await a.add(word,img[0])
        # _search_flmt.start_cd(user_id)
        await addpic.finish(Message(result))
    except Exception as e:
        print('**************************************')
        print(e)
        print('**************************************')
        # await addpic.finish("图和关键词不能一起发？")
