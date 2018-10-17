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

    def __init__(self, player, custom_io="stdio", writer=None, reader=None):
        self.player = player
        self.DATA_PATH = "./data/"
        self.handler = "init"
        self.msg = ""
        self.event = dict()
        # io:
        # stdio: for terminal
        # telnet_io: for telnet server
        self.io = custom_io
        self.writer = writer
        self.reader = reader
        # check if the record exist, if yes, load it
        if os.path.exists(self.DATA_PATH+player.name+".joblib"):
            continu = self.read("用户已经存在，继续？（y/n 选择n将开始新的游戏并删除原记录)：")
            if continu == 'y':
                self.load()
            elif continu == 'n':
                self.write("你选择了开始一个新游戏")
            msg = "欢迎%s来到恐龙世界" % self.player.name
            self.write(msg)
            print_sep()

    def get_handler(self):
        return self.handler

    def run(self, output=None):
        self.get_event()
        self._display()
        sel = input("请输入你的选择：")
        self.process_selection(sel)

    def process_handler(self, handler, sel):
        return eval(handler)(self, sel)

    def get_event(self):
        self.event = EVENTS[self.handler]

    def process_selection(self, sel):
        options = self.event['options']
        not_valid_sel, msg = self._not_valid_selection(sel, options)
        if not_valid_sel:
            return self.handler
        sel = int(sel)
        handler = self.handler
        self.handler = options[sel].split('@')[-1]
        self.msg = eval(handler)(self, sel)

    def _display(self):
        if self.msg != "":
            print_sep()
            self.write(self.msg)
        self.write(self.event["prologue"])
        options = self.event['options']
        for i in range(len(options)):
            msg = "%d, %s" % (i, options[i])
            self.write(msg)

    def _not_valid_selection(self, selection, options):
        if selection in COMMANDS:
            comm = COMMANDS[selection].split("@")[-1]
            eval(comm)(self)
            return True, "COMMAND"
        try:
            selection = int(selection)
        except:
            return True, "ERROR"
        if selection not in range(len(options)):
            return True, "ERROR"
        return False, "VALID_OPTION"


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


    def write(self, msg=""):
        """ write to self.io
        """
        if self.io == "stdio":
            print(msg)
        if self.io == "telnet_io":
            self.writer.write(msg)

    def read(self, msg=""):
        """read from self.io
        """
        if self.io == "stdio":
            ret = input(msg)
        if self.io == "telnet_io":
            self.writer.write(msg)
            ret = yield from self.reader.read(1)
        return ret

    def _check_status(self):
        """ check if the record already exist
        """
        pass
