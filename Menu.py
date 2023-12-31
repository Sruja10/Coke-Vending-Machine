from Exceptions import *


class CokeMenu:
    def __init__(self):
        # Initializing the private attributes
        self.__cokeMenu = [
            'Pepsi',
            'Sprite',
            '7Up',
            'Mountain Dew',
            'CocoCola'
        ]

    def get_menu(self):
        # Get the menu
        return self.__cokeMenu

    def menu_remove(self, coke):
        # Not used in the main.py since menu is fetched from MONEY.PY
        self.__cokeMenu.remove(coke)

    def coke_check(self, coke):
        # To check if coke is present
        if coke not in self.get_menu():
            raise NoCoke(f"Apologies! {coke} is not available. Please select another drink")
        else:
            return

    def get_coke(self, coke):
        try:
            self.coke_check(coke)
            return True
        except NoCoke as error:
            print(error)
            return False

