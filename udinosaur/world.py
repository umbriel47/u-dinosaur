""" The world class
"""
# -*- coding: utf-8 -*-

import os
import joblib

from udinosaur.registries import EVENTS, COMMANDS
from udinosaur.handlers.events import *
from udinosaur.handlers import commands
from udinosaur.aux import print_sep

class World(object):
    """The definition of the game's world"""

    def __init__(self, player):
        self.player = player
        self.DATA_PATH = "./data/"
        self.handler = "init"
        self.msg = ""
        # check if the record exist, if yes, load it
        if os.path.exists(self.DATA_PATH+player.name+".joblib"):
            continu = input("用户已经存在，继续？（y/n 选择n将开始新的游戏并删除原记录)：")
            if continu == 'y':
                self.load()
            elif continu == 'n':
                print("你选择了开始一个新游戏")
            print("欢迎%s来到恐龙世界" % self.player.name)
            print_sep()

    def get_handler(self):
        return self.handler

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
        sel = int(selection)
        opt = options[sel].split('@')[-1]
        new_handler = eval(handler)(self, sel, opt)
        return new_handler

    def show_event(self, handler):
        pass

    def process_selection(self, handler):
        pass


    def _not_valid_selection(self, selection, options):
        if selection in COMMANDS:
            comm = COMMANDS[selection].split("@")[-1]
            eval(comm)(self)
            return True
        return False


    def save(self):
        """ save the current world to a joblib file named
        by the name of the Player"""
        file_name = self.player.name + ".joblib"
        joblib.dump(self.player, self.DATA_PATH+file_name)
        save_meta = dict()
        save_meta['handler'] = self.handler
        file_name = self.player.name + ".meta"
        joblib.dump(save_meta, self.DATA_PATH+file_name)
        print("Data for %s saved successfully" % self.player.name)
        print_sep()

    def load(self):
        """load the record to the world
        """
        file_name = self.player.name + ".joblib"
        self.player = joblib.load(self.DATA_PATH+file_name)
        file_name = self.player.name + ".meta"
        self.handler = joblib.load(self.DATA_PATH+file_name)['handler']
        print("Data for %s loaded successfully" % self.player.name)
        print_sep()

    def _check_status(self):
        """ check if the record already exist
        """
        pass
