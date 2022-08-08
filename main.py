#!/usr/bin/python
from world_map import *
from paused_print import *

Question = input("Password ? ")
if(Question == 'prova'):
  printWorldMap()
else:
  console("Disconnected")