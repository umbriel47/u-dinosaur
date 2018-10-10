""" events handlers
"""

import numpy as np

from udinosaur.registries import ENTITIES
from udinosaur.config import N_MAX_PETS
from udinosaur.config import CATCH_PET_PROB
from udinosaur.entities.dinosaurs import Dinosaur
from udinosaur.aux import print_sep


def init(world, sel, opt):
    print_sep()
    if sel == 0:
        print("看起来今天天气不错啊")
    if sel == 1:
        world.player.show_pets()
        opt = "init"
    if sel == 2:
        print("怕累死，还是继续睡觉吧")
    print_sep()
    return opt

def walk_around(world, sel, opt):
    print_sep()
    if sel == 0:
        print("我要过去看看，说不定能碰到什么")
    if sel == 1:
        print("怕累死，还是回家睡觉吧")
    return opt

def catch_pet(world, sel, opt):
    print_sep()
    if sel == 0:
        if len(world.player.pets) > N_MAX_PETS:
            print("你家里已经有%d宠物了，装不下了。" % N_MAX_PETS)
        elif np.random.rand() > CATCH_PET_PROB:
            print("对方挣扎了一下，跑掉了，只剩下一个模糊的背影和一地灰尘。你决定还是回家睡觉去吧。")
        else:
            type = np.random.choice(ENTITIES["dinosaurs"])
            nickname = input("你找到了一条"+type+", 给它取个好听的名字吧：")
            dino = Dinosaur(type, nickname)
            world.player.add_pet(dino)
    if sel == 1:
        print("怕累死，还是回家睡觉去吧")
    print_sep()
    return opt
