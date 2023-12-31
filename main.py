from Menu import *
from Money import *

menu = CokeMenu()
money = MoneyInfo()

flag = True

while flag:
    choice = input("Select an option 1.Buy a drink | 2.View Money collected | 3.Exit: ")
    if choice == '1':
        print("--------------------------------")
        coke_menu = money.get_price_menu()
        for i, v in coke_menu.items():
            print(f"{i} = {v}$")
        print("--------------------------------")
        coke = input(f"Please select the coke from the menu: ")
        if menu.get_coke(coke):
            amount = int(input("Please enter the amount in $ "))
            if money.money_transaction(coke, amount):
                menu.menu_remove(coke)
                print("Enjoy your drink!!")
    elif choice == '2':
        print(f"Total amount collected in machine is: {money.get_money_collected()}")
    else:
        print("Thanks for using the machine")
        flag = False
