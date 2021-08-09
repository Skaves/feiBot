import re
import asyncio
import os
from random import choice
from nonebot.adapters.cqhttp import Bot, MessageEvent,Message,MessageSegment

from .data_source import Tuan


kaituan = Tuan().on_command(
    "开团",  "打团啦", aliases={"开团了","打团了"}
)


@kaituan.handle()
async def _kaituan(bot: Bot, event: MessageEvent):
    pic = await Tuan.totaltable()
    li = await Tuan.singlewave('1')
    if pic == -1 or li == -1:
        await kaituan.finish('error.')
    pic = os.path.join(r'file:///D:/feiBot/bot/pics',pic)
    await kaituan.send(MessageSegment.image(pic))
    aite = "开团了，"
    for i in li:
        aite += f"{MessageSegment.at(i.qq)}"+"来"+str(i.role)+"   "
    await kaituan.finish(Message(aite))


wave = Tuan().on_regex(r"第(.*?)波", "发送名单并艾特")
common_used_numerals ={'零':0, '一':1, '二':2, '两':2, '三':3, '四':4, '五':5, '六':6, '七':7, '八':8, '九':9, '十':10}

@wave.handle()
async def _wave_tuan(bot: Bot, event: MessageEvent):

    msg = str(event.message).strip()
    pattern = r"第(.*?)波"
    wv = re.findall(pattern, msg)[0]
    try:
        wv = int(wv)
    except:
        total=0
        r=1
        for i in range(len(wv) - 1, -1, -1):
            val = common_used_numerals.get(wv[i])
            if val >= 10 and i == 0:  #应对 十三 十四 十*之类
                if val > r:
                    r = val
                    total = total + val
                else:
                    r = r * val
            elif val >= 10:
                if val > r:
                    r = val
                else:
                    r = r * val
            else:
                total = total + r * val
        wv = total
    li = await Tuan.singlewave(str(wv))
    aite = "第"+str(wv)+"波了，"
    for i in li:
        aite += f"{MessageSegment.at(i.qq)}"+"来"+str(i.role)+"   "
    await kaituan.finish(Message(aite))
