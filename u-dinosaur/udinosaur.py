""" The main loop of the game
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from handlers import users
from world import World
from player import Player

def main():
    # login the player
    player = users.login()
    # init the world, if the player's save file exist, load it. Otherwise
    # start a new one
    world = World(player)
    while True:
        handler = world.run(handler)

if __name__ == "__main__":
    main()
