""" functions to manage the game
"""

import json
import re

def update_events_json(script):
    """ update the events.json file through a script
    """
    _json_file = "./events/events.json"
    _evt_file = "./events/script.evt"

    events = dict()
    with open(_evt_file, 'r') as fp:
        content = ''.join(fp.readlines())
    pat = r"#\n"
    events_lst = re.split(pat, content)
    # assumes each name, prologue and option only takes one line
    for event in events_lst:
        event = event.strip().split('\n')
        name = event[0].split(': ')[-1]
        prologue = event[1].split(': ')[-1]
        options = event[3:]
        events[name] = dict()
        events[name]["prologue"] = prologue
        events[name]["options"] = options
    json.dump(events, open(_json_file, 'w'))


if __name__ == '__main__':
    update_events_json('./events/script.evt')
