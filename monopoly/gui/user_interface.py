from typing import List
from color import Color
from gui.utils import TerminalColor

t_Tile = "Tile"
t_StreetTile = "StreetTile"

def choice(msg:str)->bool:
  c = input(f"{msg} o/n : ").lower()
  yes = ["yes", "y", "oui", "o"]
  no = ["no", "non", "n"]
  if c in yes:
    return True
  elif c in no:
    return False
  else:
    print("Invalid input selct in ", yes, " for yes, or in ", no, " for no" )
    return choice(msg)


def chooseInt(msg:str)->bool:
  i = int(input(f"{msg} : "))


def getPlayers():
  res = []
  while True:
    name = input("Entrez un nom pour ajouter un joueur (ou entrez une ligne vide pour valider) : ")
    if name != '':
      res.append(name)
    else:
      break
  if len(res)<2:
    print("Il n'y a pas assez de joeurs, veuillez recommencer")
    res = getPlayers()

  return res


def offerToBuild(streets:List[t_StreetTile]):
  if len(streets)==0:
    return []
  print("Entrez un par un les numéros des rues où vous souhaitez construire, et une ligne vide pour valider les choix des chantiers : ")


  for i, street in enumerate(streets):
    print("\n-----------------")
    print(street.getUpgradeMessage(), "(Entrez %d)"%i)
    print("-----------------")


  res = []


  while True:

    i = input( " En attente de choix ... : " )

    while True:
      if i.isdigit():
        if 0<=int(i)<len(streets):
          break
      if i=='':
        break

      i = input( "Entrée invalide!\n En attente de choix ... : " )

    if i=='':
      break
    else:
      res.append(int(i))

  return res

def bankrupt(playerName:str):
  print(f"{playerName} a fait failite !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

def display_tile(tile:t_Tile):
  print(tile)


def message(msg):
  print(msg)


def insuffisent_balence(balance):
  print(TerminalColor.ORANGE(f"Solde insuffisant : {balance}€"))



def successful_payment(prev_balance, new_balance):
  print(TerminalColor.GREEN(f"Payement effectué avec succès {prev_balance}€ -> {new_balance}€"))




def successful_debit(diff, prev_balance, new_balance):
  print(f"{TerminalColor.RED()} Encaissé {diff}€ avec succès {prev_balance}€ -> {new_balance}€{TerminalColor.RESET}")


def passed_on_go():
  print("-------------- passage par GO -------------------")


def victory(player):
  print(f"{str(player)} a Gagné !!!!!!!!!!!!!\n**************FÉLICITATION*****************")


def fatal_debit(required_money_sum, prev_balance):
  print(TerminalColor.RED(f"Votre solde de {prev_balance}€ n'a pas pu couvrir la dépense de {required_money_sum}€") )

def credit(player, diff, old_balance, new_balance):
  print(player, TerminalColor.BLUE(f" : {old_balance}€ + {diff}€  -> {new_balance}€ "))

def is_final():
  print(TerminalColor.RED("La construction a échoué!! Cette case est dans sa forme finale."))


def upgrade_successfull(street):
  print(f"Construction réussite sur {street} !")
