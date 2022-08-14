#!/usr/bin/python
from pickle import TRUE
from auth import authMe
from world_map import *
from paused_print import *
from list_of_games import listGames

if(authMe() == TRUE):
  listGames()
else:
  console("noo")

  