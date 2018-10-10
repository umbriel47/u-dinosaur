# u-dinosaur

### Introduction

A text-based game for an adventure in the dinosaur age

u-dinosaur is a single-machine text-based game that allows the player to raise pet dinosaurs.

The framework of this game supports relatively story making and each user can easily replace the story/logic with his/her own one without worrying too much about the code.

### How to make stories

To make a story different parts of the game should be changed:

1. construct the logic in a text file following the format of udinosaur/events/script.evt

  - each event is separated by "#"
  - name: name of the event, and it is the same as the event handler
  - prologue: the text user wants to display before options
  - options: the options to choose, following the format: <display text>@handler

2. compile .evt file to .json file through udinosaur/aux.update_events_json

3. register relevant events in registries

4. implement corresponding event handler in udinosaur/handlers/events.py

5. update entities in udinosaur/entities/

6. modify udinosaur/player.Player if necessary

### Versions

_v1.0_ (current)

- game framework to support story making/logic building without knowing the programming part
- save/load records (one record for each user)
- basic system functions, such as exit and help
- find and capture dinosaurs; view dinosaurs you have


_v2.0_

TBD

##
