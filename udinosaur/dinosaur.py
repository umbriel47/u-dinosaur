""" The main loop of the game
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket
import argparse

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


def socket_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 1911))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        welcome_message = '想要进入奇幻的恐龙世界么? (y/n)\n'
        conn.sendall(welcome_message.encode('utf-8'))
        res = conn.recv(1024).decode('utf-8').strip()
        print(res)
        if res == 'y':
            conn.sendall(OPENING.encode('utf-8'))
            inp = "请输入你的名字："
            conn.sendall(inp.encode('utf-8'))
            name = conn.recv(1024).decode('utf-8').strip()
            player = users.login(name)
            world = World(player, "socket_io", conn)
            while True:
                world.run()



if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="Please put in the backend \
                                    that runs the game")
    parse.add_argument('-b', '--backend', help="Put in the backend mode")
    args = parse.parse_args()
    backend = args.backend
    if backend == "terminal":
        terminal()
    elif backend == "socket":
        socket_server()
    else:
        print("Wrong parameters")
