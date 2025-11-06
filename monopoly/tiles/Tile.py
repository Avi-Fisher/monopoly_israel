from Property_tile import Property
from rent import Rent
from Bonus_tile import Bonus
from Tax_tile import Tax
from Jail_tile import Jail

class Tile():

    def check(self,tile,turn,not_turn):

        match tile["type"]:
           case "property":
               Property().property_tile(tile,turn)
           case "computer" | "player":
                Rent().rent(tile,turn,not_turn)
           case "bonus":
               Bonus().bonus(tile,turn)
           case "tax":
               Tax().tax(tile,turn)
           case "jail":
               Jail()











