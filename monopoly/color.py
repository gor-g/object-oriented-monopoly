from typing import Dict, Union
from gui.utils import TerminalColor


t_StreetTile = "StreetTile"
t_Player = "Player"

class Color:
  def __init__(self, name:str, r:int, g:int, b:int):
    self.__name:str = name
    self.__color:tuple[int,int,int] = (r, g, b)
    self._streets:list[t_StreetTile] = []

  def __str__(self):
    return f"{self.colorate_bg(self.__name)}"

  def get(self):
    return TerminalColor.rgb_to_ansi(*(self.__color))

  def update(self, street_tile:t_StreetTile):
    if self.isMonopolized():
      self.makeConstructible()

  def isMonopolized(self):
    street = self._streets[0]
    owner = street._owner
    if owner == None:
      return False
    for street in self._streets:
      if owner != street._owner:
        return False
    return True

  def isFullyOwnedBy(self, player:t_Player):
    return self._streets[0]._owner == player and self.isMonopolized()

  def displayOwner(self):
    for street in self._streets:
      print(street, " : ", street._owner._name)

  def makeConstructible(self):
    for street in self._streets:
      street.makeConstructible()


  # --------------------
  # interface functions

  def bg(self):
    return TerminalColor.rgb_to_ansi(*(self.__color), True)

  def fg(self):
    return TerminalColor.rgb_to_ansi(*(self.__color), False)

  def colorate_bg(self, s):
    return self.bg() + s + TerminalColor.RESET

  def colorate_fg(self, s):
    return self.fg() + s + TerminalColor.RESET
