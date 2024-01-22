from typing import Union, TypeVar
from monopoly import *
from gui.utils import *

t_Tile = "Tile"
t_StreetTile = "StreetTile"

class TextRow:
  body = None

  def display(self):
    print(self.body, end='')


class TextContentfullRow(TextRow):

  def __init__(self, width, content: str):
    assert (width >= len(content) + 2), "Row content is longer than the line width"


class TextRowCentered(TextContentfullRow):

  def __init__(self, width: int, content: str = '', color: str = TerminalColor.RESET, border: str = 'solid'):
    super(TextRowCentered, self).__init__(width, content)

    self.__content: str = content
    self.__width: int = width
    self.__color: color = color

    if border == "solid":
        self.__border = "\u2502"
    elif border == "none":
        self.__border = " "

    self.__lfiller, self.__rfiller = self.__computeFillers()

    self.__recomputeBody()

  def __recomputeBody(self):

    self.body =   self.__border \
                + self.__color \
                + self.__lfiller \
                + self.__content \
                + self.__rfiller \
                + TerminalColor.RESET \
                + self.__border

  def __computeFillers(self):

    width_lfiller: int = (self.__width - len(self.__content) - 2 * len(self.__border)) // 2
    lfiller: str = ' ' * width_lfiller
    rfiller: str = ' ' * (self.__width - len(self.__content) - 2 * len(self.__border) - width_lfiller)

    return lfiller, rfiller

  def display(self):
    print(self.body, end='')


class TextTopRow(TextRow):
  def __init__(self, width: int, color: str = TerminalColor.RESET, border: str = 'solid'):

    self.__width: int = width
    self.__color: color = color

    if border == "solid":
        self.body = self.__color + "\u250C" + "\u2500" * (width - 2) + "\u2510" + TerminalColor.RESET
    elif border == "none":
        self.body = " " * width


class TextBottomRow(TextRow):
  def __init__(self, width: int, color: str = TerminalColor.RESET, border: str = 'solid'):

    self.__width: int = width
    self.__color: color = color

    if border == "solid":
        self.body = self.__color + "\u2514" + "\u2500" * (width - 2) + "\u2518" + TerminalColor.RESET
    elif border == "none":
        self.body = " " * width


class TextSeparatorRow(TextRow):
  def __init__(self, width: int, color: str = TerminalColor.RESET, border: str = 'solid'):

    self.__width: int = width
    self.__color: color = color

    if border == "solid":
      self.body = self.__color + \
                  "\u251C" + "\u2500" * (width - 2) + "\u2524" \
                  + TerminalColor.RESET
    elif border == "none":
      self.body = " " * width


TextTopRow(width=30).display()
print()
TextRowCentered(width=30, content="smth").display()
print()
TextSeparatorRow(width=30).display()
print()
TextBottomRow(width=30).display()


class TextTile:
  defaultSide: int = 10
  terrainColorBarThickness = 2
  body: list
  _w: int
  color: str

  def displaySolo(self):
    for row in self.body:
      row.display()
      print()

  def updatePriceRow(self, content):
    self.body[-2] = TextRowCentered(content=content, width=self._w, color=self.color)
    return self


class BasicTextTile(TextTile):
  def __init__(self, side: int = TextTile.defaultSide, border="solid", color=TerminalColor.RESET):
    self._w: int = int(side * 2.4)
    self.__h: int = side
    self.color: str = color

    self.__top: TextRow = TextTopRow(width=self._w, border=border, color=color)
    self.__bottom: TextRow = TextBottomRow(width=self._w, border=border, color=color)
    self.__empty: TextRow = TextRowCentered(width=self._w, border=border, color=color)

    self.body = [self.__top] + [self.__empty for _ in range(self.__h - 2)] + [self.__bottom]


class GoTextTile(BasicTextTile):
  def __init__(self, content: t_StreetTile, side: int = TextTile.defaultSide):
    super(GoTextTile, self).__init__(side=side, border="solid", color=TerminalColor.RESET)

    self.content = content

    self.setName()



  def setName(self):
    r = 1 + TextTile.terrainColorBarThickness + 1  # on saute la première ligne qui est la bordure, puis
    # l'épaisseur de la bare de couleur, puis encore 1 ligne
    self.body[r] = TextRowCentered(content=self.content.title.upper(), width=self._w)



class StreetTextTile(BasicTextTile):
  def __init__(self, content: t_StreetTile, side: int = TextTile.defaultSide):
    super(StreetTextTile, self).__init__(side=side, border="solid", color=TerminalColor.RESET)

    self.content = content
    self.__topColor = TerminalColor.rgb_to_ansi(*(self.content._color), is_background=True)

    self.colorateTop()
    self.updatePriceRow(self.content._price)
    self.setName()

  def colorateTop(self):
    for r in range(1, 1 + TextTile.terrainColorBarThickness):
      self.body[r] = TextRowCentered(content='', width=self._w, color=self.__topColor)

  def setName(self):
    r = 1 + TextTile.terrainColorBarThickness + 1  # on saute la première ligne qui est la bordure, puis
    # l'épaisseur de la bare de couleur, puis encore 1 ligne
    self.body[r] = TextRowCentered(content=self.content.title.upper(), width=self._w)


