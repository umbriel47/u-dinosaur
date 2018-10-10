"""registries for events and entities
"""
# -*- coding: utf-8 -*-

import json

EVENTS = json.load(open("./events/events.json", 'r'))


# entities designed for the game
ENTITIES = {
"dinosaurs": ["霸王龙", "腕龙", "翼龙", "三角龙", "雷龙", "马门溪龙", "迅猛龙"],
"items": ["Knief", "Stick"]
}


# system command of the game
COMMANDS = {
"save": "保存游戏@commands.save",
"load": "读取存档@commands.load",
"exit": "退出游戏@commands.exit_game",
"help": "显示该条帮助@commands.help"
}

# the areas on the map
LOCATIONS = {
"home": {
    "type": "land"
},
"wetland": {
    "type": "lake"
}
}
