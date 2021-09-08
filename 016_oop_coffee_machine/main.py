from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while True:
    choice = input("What would you like to buy (" + menu.get_items() +")?")
    if choice == 'help':
        print("type: 'help', 'report', 'fill', 'off'")
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice =='fill':
        coffee_maker.fill_resources()
    elif choice == 'off':
        break
    else:
        drink = menu.find_drink(choice)
        print(f"{choice.title()} costs {drink.cost} moneys")
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
