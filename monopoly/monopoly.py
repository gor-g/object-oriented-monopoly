from player import Player
from color import Color
from typing import List, Dict
from gui import user_interface as ui
from copy import copy

#TODO :  patterne observeur observable entre utilisateur et rue possedés



class Monopoly():
  def __init__(self, goTile, colors:List[Color]):
    self._goTile:GoTile = goTile
    self.__colors:List[Color] = colors
    self.__players:List[Player] = {Player(name, self) for name in ui.getPlayers()}

  def getTotallyOwnedColors(self, player:Player)->List[Color]:
    res = []
    for color in self.__colors:
      if color.isFullyOwnedBy(player):
        res.append(color)
    return res

  def run(self):
    while True:
      for player in self.__players:
        if player._is_in_game:
          player.play()
          players_in_game = [player for player in self.__players if player._is_in_game]
          if len(players_in_game)==1:
            ui.victory(player)
            exit(0)




