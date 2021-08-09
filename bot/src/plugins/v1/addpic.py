from nonebot import CommandSession,on_command
from nonebot.permission import *
import json
import os


@on_command('新增图片', permission=SUPERUSER)
async def addpic(session: CommandSession):
    pic = session.get('pic')
    await session.send(pic)


@addpic.args_parser
async def _(session: CommandSession):
    img = session.current_arg_images
    name = session.current_arg_text.strip()
    if not name:
        session.finish('请按 新增图片 关键词 图片 的形式发送')
    try:
        from sqlalchemy.orm import sessionmaker
        from awesome.models import DBSession,PICS
        dbsession = DBSession()
        try:
            result = dbsession.query(PICS).filter(PICS.name==str(name)).one()
            dbsession.close()
            session.state[session.current_key] = '关键词重复'
        except:
            import time
            import urllib
            t = time.time()
            fn = int(round(t * 1000000))
            fname = './pics/'+str(fn)
            urllib.request.urlretrieve(img[0], filename=fname)
            data = PICS(name=str(name),path=str(fn))
            dbsession.add(data)
            dbsession.commit()
            dbsession.close()
            session.finish('搞定')
    except Exception as e:
        print(e)
        session.state[session.current_key] = '出错啦'



    


    
