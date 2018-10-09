""" The world class
"""
# -*- coding: utf-8 -*-

import joblib

from udinosaur.registries import EVENTS, COMMANDS
from udinosaur.handlers.events import *
from udinosaur.handlers import commands

class World(object):
    """The definition of the game's world"""

    def __init__(self, player):
        self.player = player
        self.DATA_PATH = "./data/"
        # check if the record exist, if yes, load it

    def run(self, handler):
        # get the event content
        event = EVENTS[handler]
        # print the prologue
        print(event['prologue'])
        # print the options
        options = event['options']
        for i in range(len(options)):
            print("%d, %s" % (i, options[i]))
        self.handler = handler
        selection = input("请输入你的选择：")
        # check if the selection is not a valid one or a command
        if self._not_valid_selection(selection, options):
            return self.handler
        # return the new handler
        return eval(handler)(selection, options)

    def _not_valid_selection(self, selection, options):
        if selection in COMMANDS:
            comm = COMMANDS[selection]
            eval(comm)(self)
            return True
        return False


    def save(self):
        file_name = self.player.name + ".joblib"
        joblib.dump(self.player, self.DATA_PATH+file_name)
        save_meta = dict()
        save_meta['handler'] = self.handler
        file_name = self.player.name + ".meta"
        joblib.dump(save_meta, self.DATA_PATH+file_name)
        print("Data for %s saved successfully" % self.player.name)

    def load(self):
        file_name = self.player.name + ".joblib"
        self.player = joblib.load(self.DATA_PATH+file_name)
        file_name = self.player.name + ".meta"
        self.handler = joblib.load(self.DATA_PATH+file_name)['handler']
        print("Data for %s loaded successfully" % self.player.name)

    def _check_status(self):
        """ check if the record already exist
        """
        pass
