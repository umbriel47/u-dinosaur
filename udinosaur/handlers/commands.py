""" The commands handlers
"""
# -*- coding: utf-8 -*-

from udinosaur.registries import COMMANDS
from udinosaur.aux import print_sep

def save(world):
    """ save the world's status
    """
    world.save()

def load(world):
    """ load the world status
    """
    world.load()

def exit_game(world):
    """ exit the game
    """
    exit(0)

def help(world):
    """ display the help
    """
    print_sep()
    print("以下为系统命令，可随时输入使用：")
    for k, v in COMMANDS.items():
        print("%s: %s" % (k, v))
    print_sep()
