""" telnet server for the game
"""
# -*- coding: utf-8 -*-


import os
import asyncio
import telnetlib3

from udinosaur.handlers import users
from udinosaur.world import World
from udinosaur.player import Player
from udinosaur.aux import print_sep


OPENING = """很久很久以前，有人挖到恐龙化石的时候意外地发现了一个漩涡。
有几个人走到了漩涡里，来到了一个恐龙世界。
这是一个奇妙的恐龙世界。在这里你可以找到你自己的宠物。你的宠物级别越高，你就越容易在这个世界里生存下去。
宠物还会一代一代地繁殖。你的宠物还会喜欢上别的恐龙，很幸福地在一起。
让我们进入这个奇妙的恐龙世界"""

@asyncio.coroutine
def shell(reader, writer):
    writer.write('\r\nWould you like to play a game? ')
    inp = yield from reader.read(1)
    # start the game
    if inp == 'y':
        writer.write(OPENING)
        print_sep()
        # login the player
        player = users.login()
        print_sep()
        # init the world, if the player's save file exist, load it. Otherwise
        # start a new one
        world = World(player)
        while True:
            world.run(output)

    writer.close()

loop = asyncio.get_event_loop()
coro = telnetlib3.create_server(port=6023, shell=shell)
server = loop.run_until_complete(coro)
loop.run_until_complete(server.wait_closed())
