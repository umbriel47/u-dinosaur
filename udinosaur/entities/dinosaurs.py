""" Defines the dinosaurs in the world
"""
# -*- coding: utf-8 -*-

class Dinosaur(object):
    """ base class for dinosaur
    """

    def __init__(self, type="", nickname=""):
        self.type = type
        self.nickname = nickname

    def show(self):
        msg = ""
        msg += "-" * 10 + "\n"
        msg += "昵称：" + self.nickname + "\n"
        msg += "恐龙类型：" + self.type + "\n"
        return msg
