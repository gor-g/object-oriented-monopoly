from numpy import infty
import gui.user_interface as ui
from gui.text_tile import *
import gui.images as images
from typing import Union
from monopoly import *

t_Player = "Player"
t_Color = "Color"
t_StreetTile = "StreetTile"

class Tile:

  def __init__(self, title ):
    self.title = title
    self._owner = None
    self._next = self

  def __str__(self):
    return f"Tile: {self.title} - Type: {str(type(self))}"

  def insertHead(self, newTile):
    newTile._next = self._next
    self._next = newTile
    return newTile

  def nStepsForward(self, n:int, player:t_Player): # gg - player est utilisé seulement lors du passage au Go
    assert n > 0

    if n==1:
      return self._next
    else:
      return self._next.nStepsForward(n-1, player)

  def dispAll(self):
    print("here2", str(self))
    curr = self._next
    while curr!=self:
      print("here1",str(curr))
      curr = curr._next





class GoTile(Tile):
  def __int__(self, title="Go"):
    super(GoTile, self).__init__(title)

  def playerLanded(self, player:t_Player):
    ui.display_tile(self)

  def nStepsForward(self, n:int, player:t_Player):
    assert n > 0

    ui.passed_on_go()
    player.credit(200)

    if n==1:
      return self._next
    else:
      return self._next.nStepsForward(n-1, player)



# virtual
class PropertyTile(Tile):

  def __init__(self, title:str, price:int):
    super(PropertyTile, self).__init__(title)
    self._price:int = price
    self._owner:Union[t_Player, None] = None

  def getPrice(self)->int:# overrid in subclass : StreetTile
    return self._price




class StreetTile(PropertyTile):
  class State:


    def notify(self):
      return self._obj._color.update(self._obj)

    def playerLanded(self, player: t_Player): # overrid in states : Ownerless
      ui.display_tile(self._obj)
      owner = self.getOwner()
      if owner != player :
        fee = self.computeFee()
        player.debit(fee)
        owner.credit(fee)

    def isUpgradable(self): # overrid in states : Constructible, Hotelable
      return False

    def getPrice(self): # overrid in states : Ownerless
      raise NotImplementedError("This method isn't implemented for the state %s"%str(type(self)))

    def upgrade(self): # overrid in states : Constructible, Hotelable
      raise NotImplementedError("This method isn't implemented for the state %s"%str(type(self)))

    def getUpgradeMessage(self):
      raise NotImplementedError("This method isn't implemented for the state %s"%str(type(self)))

    def setOwner(self, owner:t_Player):
      self._obj._owner = owner
      self._obj.setState(StreetTile.Owned(self._obj))
      self.notify()

    def makeConstructible(self):
      raise NotImplementedError("This method isn't implemented for the state %s"%str(type(self)))

    def getOwner(self):
      return self._obj._owner

    def getFootRow(self): # overrid in states : Ownerless
      return f"Appeartiens à {self.getOwner()}€"


  class Ownerless(State):

    def __init__(self, obj:t_StreetTile):
      self._obj:t_StreetTile = obj
      self.notify()

    def playerLanded(self, player: t_Player):
      ui.display_tile(self._obj)
      if player.offerToBuy(self._obj):
        if player.pay(self.getPrice()):
          self.setOwner(player)


    def descr(self):
      return {}

    def computeFee(self):
      return 0

    def getPrice(self):
      return self._obj._price

    def getPriceRow(self):
      return f"À vendre : {self.getPrice()}€"


  class Owned(State):

    def __init__(self, obj:t_StreetTile):
      self._obj:t_StreetTile = obj
      self.notify()

    def computeFee(self):
      return self._obj._rents[0]


  class Constructible(State):
    def __init__(self, obj:t_StreetTile):
      self._obj:t_StreetTile = obj
      self.__numberOfHouses = 0

    def computeFee(self):
      return self._obj._rents[self.__numberOfHouses]

    def upgrade(self):
      if self.__numberOfHouses < 3:
        self.__numberOfHouses +=1
      else:
        self._obj.setState(StreetTile.Hotelable(self._obj))
      ui.upgrade_successfull(self._obj.__str__())
      return True

    def getUpgradeMessage(self):
      return f"{str(self._obj)} :\n{self.__numberOfHouses} maisons construites \nPayer {self._obj._construction_cost}€ pour construire une maison"

    def isUpgradable(self):
      return True


  class Hotelable(State):
    def __init__(self, obj:t_StreetTile):
      self._obj:t_StreetTile = obj

    def computeFee(self):
      return self._obj._rents[4]

    def upgrade(self):
      self._obj.setState(StreetTile.Final(self._obj))
      ui.upgrade_successfull(self._obj.__str__())

      return True

    def getUpgradeMessage(self):
      return f"{str(self._obj)} :\n4 maisons construites \nPayer {self._obj._construction_cost}€ pour construire un hotel"

    def isUpgradable(self):
      return True


  class Final(State):
    def __init__(self, obj:t_StreetTile):
      self._obj:t_StreetTile = obj

    def computeFee(self):
      return self._obj._rents[-1]

    def upgrade(self):
      ui.is_final()




  def __init__(self, title:str, color:t_Color, price:int, construction_cost:int,  rents:list[int] ):
    super(StreetTile, self).__init__(title, price)

    self.attache(color)
    self._construction_cost = construction_cost
    self._rents = rents
    self.setState(StreetTile.Ownerless(self))

  def __str__(self):
    return f"{self._color.colorate_bg(self.title)}"

  def attache(self, color):
    self._color = color
    print("here3", color)
    color._streets.append(self)

  def playerLanded(self, player: t_Player):
    self.__state.playerLanded(player)

  def setState(self, new_state:State ):
    self.__state = new_state

  def makeConstructible(self):
    self.setState(StreetTile.Constructible(self))

  def getPrice(self):
    return self.__state.getPrice()

  def computeFee(self):
    return self.__state.computeFee()

  def upgrade(self):
    self.__state.upgrade()

  def getUpgradeMessage(self):
    return self.__state.getUpgradeMessage()

  def getPriceRow(self):
    return self.__state.getFootRow()

  def isUpgradable(self):
    return self.__state.isUpgradable()


class TrainStationTile(PropertyTile):
  def __int__(self, title:str, price:int):
    super(TrainStationTile, self).__init__(title, price)

  def __str__(self):
    return f"{self.title}\n{images.train}"

  def computeFee(self):
    owner:Union[t_Player, None ] = self._owner
    if owner is None:
      return 0
    else:
      assert 4 >= owner.getNumberOfTrainStations() > 0
      return [0,25, 50, 100, 200][owner.getNumberOfTrainStations()]


  def getPriceRow(self): # overrid in states : Ownerless
    owner = self._owner
    if owner is not None:
      return f"Appeartiens à {self._owner}€"
    else:
      return f"À vendre : {self._owner}€"


  def playerLanded(self, player: t_Player):# overrid in subclass : StreetTile
    ui.display_tile(self)
    owner = self._owner
    if owner is None:
      if player.offerToBuy(self):
        if player.pay(self.getPrice()):
          self._owner = player
          player.incrementNumberOfTrainStations()

    elif owner != player:
      fee = self.computeFee()
      player.debit(fee)
      owner.credit(fee)

class UtilityTile(PropertyTile):
  __base_fee = 1

  def __int__(self, title:str, price:int):
    super(UtilityTile, self).__init__(title, price)


  def computeFee(self):
    owner:Union[t_Player, None ] = self._owner
    if owner is None:
      return 0
    else:
      assert 0 < owner.getNumberOfUtilities() <= 2
      return [0, 4, 10][owner.getNumberOfUtilities()]*self.__base_fee*owner.rollDices()


  def playerLanded(self, player: t_Player):# overrid in subclass : StreetTile
    ui.display_tile(self)
    owner = self._owner
    if owner is None:
      if player.offerToBuy(self):
        if player.pay(self.getPrice()):
          self._owner = player
          player.incrementNumberOfUtilities()

    elif owner != player:
      fee = self.computeFee()
      balence = player.debit(fee)
      owner.credit(fee)
