class Property():

    @staticmethod
    def property_tile(tile,turn):

        if turn.name == "computer":
            if  turn.muney > tile["price"]:

                turn.muney -= tile["price"]
                turn.porperty.append(tile)

        else:

            if input("Are you wont buy this property? (yes/no)") == "yes":

                if turn.name == "computer":

                    if turn.muney > tile["price"]:
                        turn.muney -= tile["price"]
                        turn.porperty.append(tile)





























