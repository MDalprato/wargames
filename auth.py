#!/usr/bin/python
from pickle import FALSE, TRUE
from world_map import *
from paused_print import *

password = "prova"

def authMe():
  InputPsw = input("Password ? ")
  if(InputPsw == password):
    return TRUE
  else:
    console("Wrong password\n")
    console("Disconnected\n")  
    return FALSE