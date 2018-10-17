""" user administration
"""

from udinosaur.player import Player

def login(name="无名"):
    player = Player(name)
    return player
