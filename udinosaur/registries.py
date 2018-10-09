"""registries for events and entities
"""
# -*- coding: utf-8 -*-

import json

EVENTS = json.load(open("./events/events.json", 'r'))

ENTITIES = {
"dinosaurs": ["BaWangLong", "WanLong"],
"items": ["Knief", "Stick"]
}

COMMANDS = {
"save": "commands.save",
"load": "commands.load"
}

LOCATIONS = {
"home": {
    "type": "land"
},
"wetland": {
    "type": "lake"
}
}
