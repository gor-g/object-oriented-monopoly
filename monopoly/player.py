from dice import Dice
from typing import List
from gui import user_interface as ui
from gui.utils import TerminalColor

t_Monopoly = "Monopoly"
t_Tile = "Tile"
t_PropertyTile = "PropertyTile"

t_StreetTile = "StreetTile"
t_Color = "Color"



class Player:
  __dice1:Dice = Dice()
  __dice2:Dice = Dice()

  def __init__(self, name:str, monopoly:t_Monopoly ):
    self._name = name
    self.__balance:int = 10033
    self.__monopoly:t_Monopoly = monopoly
    self.__tile:t_Tile = monopoly._goTile
    self.__number_of_train_stations:int = 0
    self.__number_of_utilities:int = 0
    self._is_in_game = True
    self.__display_color = TerminalColor.random_color(10, 100, True)

  def __str__(self):
    return f"{self.__display_color}  {self._name}  {TerminalColor.RESET}"

  def offerToBuy(self, propTile:t_PropertyTile ):
    return ui.choice(msg = "Acheter la case pour %d€?" % propTile.getPrice())

  def offerToBuild(self, userColors:List[t_Color]):

    upgradeable_streets:List[t_StreetTile] = []
    for color in userColors:
      for street in color._streets:
        if street.isUpgradable():
          upgradeable_streets.append(street)


    indx_streest_to_upgrade = ui.offerToBuild(upgradeable_streets)

    for i in indx_streest_to_upgrade:
      street = upgradeable_streets[i]
      if street.isUpgradable():
        if self.pay(street._construction_cost):
          street.upgrade()
      else:
        ui.is_final()


  def pay( self, sumOfMoney:int ):
    if sumOfMoney > self.__balance:
      ui.insuffisent_balence(self.__balance)
      return False
    else:
      prev_balance = self.__balance
      self.__balance -= sumOfMoney
      ui.successful_payment(prev_balance, self.__balance)
      return True

  def debit( self, sumOfMoney:int ): # gg - la difference avec pay() c'est que ce n'est pas une action volontaire, donc s'il n'a pas assez d'argent il fait faillite
    if sumOfMoney > self.__balance:
      ui.fatal_debit(sumOfMoney, self.__balance)
      self.__balance = 0
      self.declare_bankrupt()
    else:
      prev_balance = self.__balance
      self.__balance -= sumOfMoney
      ui.successful_debit(sumOfMoney, prev_balance, self.__balance)

  def credit(self, sumOfMoney:int ):
    old_balance = self.__balance
    self.__balance += sumOfMoney
    ui.credit(str(self), sumOfMoney, old_balance, self.__balance )

  def declare_bankrupt(self):
    self._is_in_game = False
    ui.bankrupt(str(self))

  def getNumberOfTrainStations(self):
    return self.__number_of_train_stations

  def incrementNumberOfTrainStations(self):
    self.__number_of_train_stations+=1

  def getNumberOfUtilities(self):
    return self.__number_of_utilities

  def incrementNumberOfUtilities(self):
    self.__number_of_utilities+=1


  @classmethod
  def rollDices(cls):
    return cls.__dice1.roll() + cls.__dice2.roll()

  def play(self):
    steps = 1#self.rollDices()
    ui.message(f"\n\n {str(self)} a joué. \nVotre solde est de {self.__balance}€ \nLes dés ont donné {steps}. ")
    self.__tile = self.__tile.nStepsForward(steps, self)
    self.__tile.playerLanded(self)

    userColors = self.__monopoly.getTotallyOwnedColors(self)


    if len(userColors):
      self.offerToBuild(userColors)



