""" The main loop of the game
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import asyncio
import telnetlib3

from udinosaur.handlers import users
from udinosaur.world import World
from udinosaur.player import Player
from udinosaur.aux import print_sep
from udinosaur.events.script import OPENING


def terminal():
    os.system("clear")
    print(OPENING)
    print_sep()
    # login the player
    name = input("请输入你的名字：")
    player = users.login(name)
    print_sep()
    # init the world, if the player's save file exist, load it. Otherwise
    # start a new one
    world = World(player)
    while True:
        world.run()

#telnet server for the game
@asyncio.coroutine
def shell(reader, writer):
    writer.write('\r\n想要进入奇幻的恐龙世界么? (y/n)')
    inp = yield from reader.read(1)
    # start the game
    if inp == 'y':
        writer.write(OPENING)
        print_sep()
        # login the player
        writer.write('请输入你的名字：')
        name = yield from reader.read(1)
        player = users.login(name)
        print_sep()
        # init the world, if the player's save file exist, load it. Otherwise
        # start a new one
        world = World(player, writer, reader)
        while True:
            world.run()
    writer.close()

def telnet():
    loop = asyncio.get_event_loop()
    coro = telnetlib3.create_server(port=6023, shell=shell)
    server = loop.run_until_complete(coro)
    loop.run_until_complete(server.wait_closed())



if __name__ == "__main__":
    telnet()
