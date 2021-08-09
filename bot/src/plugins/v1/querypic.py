from nonebot import CommandSession,on_command
from nonebot.permission import *
import os


@on_command('查询', aliases=('q','查'), only_to_me=False)
async def querypic(session: CommandSession):
    pi = session.get('pic')
    report = await query_from_db(str(pi))
    await session.send(report)


@querypic.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['pic'] = stripped_arg
            return

    if not stripped_arg:
        session.finish('你寻思啥呢不能搁一句话说完')


async def query_from_db(p: str):
    try:
        from sqlalchemy.orm import sessionmaker
        from awesome.models import DBSession,PICS
        dbsession = DBSession()
        result = dbsession.query(PICS).filter(PICS.name==p).one()
        filename = './pics/{}.jpg'.format(result.path)
        dbsession.close()
        return {"type": 'image',"data": {"file": filename}}
    except Exception as e:
        print(e)
        return "查无此图"

