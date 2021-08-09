#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nonebot
from nonebot.adapters.cqhttp import Bot as CQHTTPBot
from src.config import RUNTIME_CONFIG

# Custom your logger
# 
# from nonebot.log import logger, default_format
# logger.add("error.log",
#            rotation="00:00",
#            diagnose=False,
#            level="ERROR",
#            format=default_format)

# You can pass some keyword args config to init function
nonebot.init(**RUNTIME_CONFIG)
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter("cqhttp", CQHTTPBot)
if 1:
    nonebot.load_builtin_plugins()
nonebot.load_from_toml("pyproject.toml")
nonebot.load_plugins("src/plugins")

# Modify some config / config depends on loaded configs
# 
# config = driver.config
# do something...


if __name__ == "__main__":
    # nonebot.logger.warning("Always use `nb run` to start the bot instead of manually running!")
    nonebot.run(app="__mp_main__:app")
