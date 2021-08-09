from nonebot import on_command, CommandSession
import json
import os


# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名「天气」「天气预报」「查天气」
@on_command('shpm', aliases=('排名','打桩','神话排名','神话'))
async def shpm(session: CommandSession):
    # 从会话状态（session.state）中获取城市名称（city），如果当前不存在，则询问用户
    prof = session.get('prof', prompt='请输入职业名：')
    # 获取城市的天气预报
    report = await get_data_of_prof(prof)
    # 向用户发送天气预报
    await session.send(report)


# weather.args_parser 装饰器将函数声明为 weather 命令的参数解析器
# 命令解析器用于将用户输入的参数解析成命令真正需要的数据
@shpm.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()
    print("arggs:"+stripped_arg)
    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将城市名跟在命令名后面，作为参数传入
            # 例如用户可能发送了：天气 南京
            session.state['prof'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要查询的职业不能为空。')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg


async def get_data_of_prof(prof: str) -> str:
    ret=''
    uri=''
    with open('trans.json','r',encoding='utf-8') as f:
        # r=f.read()
        profs=json.load(f)
        for i in profs['zhiye']:
            if prof in i['nick']:
                uri=i['uri']
                break
    if uri=='':
        return '搞点正常的职业名'
    filename = './data/'+uri+'/shenhua.txt'
    if not os.path.exists(filename):
        return '没算，等死吧'
    with open(filename,'r',encoding='utf-8') as f:
        ret=f.read()
    return ret
