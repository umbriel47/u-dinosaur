""" events handlers
"""

import numpy as np

from udinosaur.registries import ENTITIES
from udinosaur.config import N_MAX_PETS
from udinosaur.config import CATCH_PET_PROB
from udinosaur.entities.dinosaurs import Dinosaur
from udinosaur.aux import print_sep


def init(world, sel):
    if sel == 0:
        msg = "看起来今天天气不错啊"
    if sel == 1:
        msg = world.player.show_pets()
        world.handler = "init"
    if sel == 2:
        msg = "怕累死，还是继续睡觉吧"
    return msg

def walk_around(world, sel):
    if sel == 0:
        msg = "我要过去看看，说不定能碰到什么"
    if sel == 1:
        msg = "怕累死，还是回家睡觉吧"
    return msg

def catch_pet(world, sel):
    if sel == 0:
        if len(world.player.pets) > N_MAX_PETS:
            msg = "你家里已经有%d宠物了，装不下了。" % N_MAX_PETS
        elif np.random.rand() > CATCH_PET_PROB:
            msg = "对方挣扎了一下，跑掉了，只剩下一个模糊的背影和一地灰尘。你决定还是回家睡觉去吧。"
        else:
            type = np.random.choice(ENTITIES["dinosaurs"])
            nickname = world.read("你找到了一条"+type+", 给它取个好听的名字吧：")
            dino = Dinosaur(type, nickname)
            world.player.add_pet(dino)
            msg = ""
    if sel == 1:
        msg = "怕累死，还是回家睡觉去吧"
    return msg
