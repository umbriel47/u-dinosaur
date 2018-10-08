""" The world class
"""
# -*- coding: utf-8 -*-

from udinosaur.registries import EVENTS
from udinosaur.handlers.events import *

class World(object):
    """The definition of the game's world"""

    def __init__(self, player):
        self.player = player
        # check if the record exist, if yes, load it

    def run(self, handler):
        event = EVENTS[handler]
        print(event['prologue'])
        options = event['options']
        for i in range(len(options)):
            print("%d, %s" % (i, options[i]))
        selection = input("请输入你的选择：")
        # check if the selection is not a valid one or a command
        if self._not_valid_selection(selection, options):
            return handler
        # return the new handler
        return eval(handler)(selection, options)

    def _not_valid_selection(self, selection, options):
        return False

    def save(self):
        pass

    def _check_status(self):
        pass
