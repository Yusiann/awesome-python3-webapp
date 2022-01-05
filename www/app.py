#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 通过logging.basicConfig函数对日志的输出格式及方式做相关配置,日志的输出等级是INFO，意思是INFO级别以上的日志才会输出。
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web 

# 此函数作用为处理URL
def index(request):
    return web.Response(body=b'<h1>My Blog</h1>',content_type='text/html') #构造一个HTTP响应

# @asyncio.coroutine 在版本3已经改成async def的格式，更加简便
async def init(loop):
    # 创建Web服务器实例app，也就是aiohttp.web.Application类的实例，该实例的作用是处理URL、HTTP协议
    app = web.Application(loop=loop)
    # 将处理函数注册进其应用路径(Application.router)
    app.router.add_route('GET', '/', index)
    # 用协程创建监听服务，并使用aiohttp中的HTTP协议簇(protocol_factory)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    # 日志输出
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

# 创建协程，初始化协程，返回监听服务，进入协程执行
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()