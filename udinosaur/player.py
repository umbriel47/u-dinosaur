""" The player class
"""
# -*- coding: utf-8 -*-

from udinosaur.aux import print_sep

class Player(object):
    """ the player class
    """
    def __init__(self, name="无名"):
        self.name = name
        # define player properties
        # this part changes for different games

        # list of pets
        self.pets = []

    def show_pets(self):
        """ show the list of pets
        """
        if len(self.pets) > 0:
            msg = ""
            counter = 0
            for pet in self.pets:
                counter += 1
                msg += "pet no.: %d\n" % counter
                print_sep()
                msg += pet.show()
                print_sep()
            print_sep()
            msg += "总共有%d个宠物，你不再孤独" % counter
        else:
            msg = "你还没有找到恐龙宠物，加油啊！"
        return msg

    def add_pet(self, pet):
        self.pets.append(pet)
