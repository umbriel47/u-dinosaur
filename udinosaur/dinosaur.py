""" The main loop of the game
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from udinosaur.handlers import users
from udinosaur.world import World
from udinosaur.player import Player

def main():
    # login the player
    player = users.login()
    # init the world, if the player's save file exist, load it. Otherwise
    # start a new one
    world = World(player)
    handler = 'init'
    while True:
        handler = world.run(handler)

if __name__ == "__main__":
    main()
