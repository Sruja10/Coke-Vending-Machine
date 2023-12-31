from Exceptions import *


class MoneyInfo:
    def __init__(self):
        # Initializing the private attributes
        self.__moneyCollected = 0
        self.__priceMenu = {
            'Pepsi': 4,
            'Sprite': 4,
            '7Up': 5,
            'Mountain Dew': 10,
            'CocoCola': 5
        }

    def get_price_menu(self):
        # Get the price menu
        return self.__priceMenu

    def get_money_collected(self):
        # get the money collected
        return str(self.__moneyCollected)+'$'

    def set_money_collected(self, value):
        # Update the money collected machine after purchasing a drink
        self.__moneyCollected += value

    def money_check(self, coke, amount):
        # To check if entered amount is sufficient/valid
        price_menu = self.get_price_menu()
        if amount < 0:
            raise InvalidAmount("Please insert a valid amount")
        elif price_menu[coke] > amount:
            raise InsufficientAmount(f"Apologies!, {amount}$ is insufficient to get {coke}.Money refunded")

    def money_transaction(self, coke, amount):
        # Money transaction
        try:
            # print("Insert the amount: ")
            price_menu = self.get_price_menu()
            self.money_check(coke, amount)
            price_of_coke = price_menu[coke]
            if amount > price_of_coke:
                balance = amount - price_of_coke
                print("Transaction successful")
                print(f"Here's your balance amount: {balance} $")
                self.set_money_collected(price_of_coke)
            else:
                self.set_money_collected(amount)
            self.get_price_menu().pop(coke)
            return True

        except InsufficientAmount as error:
            print(error)
            return False

        except InvalidAmount as error:
            print(error)
            return False

        except TypeError as error:
            print(error)
            return False



